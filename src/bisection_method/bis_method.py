from typing import Callable, Tuple, List        # Type hint
from sympy import Integer, Float, oo, zoo, nan  # Type hint and undeterminates

# root not on interval, image_a * image_b > 0
from .bis_exceptions import NotInInterval

# Image of half point (a + b) / 2 is indeterminated aka not continous, e.g 1/0
from .bis_exceptions import NotContinous

# Function doesn't contain variable
from .bis_exceptions import NoVariableInFunction

# e.g f(x, y) -> x^2 + y^2
from .bis_exceptions import MultipleVariablesInFunction

# Interval is not exactly [a, b]
from .bis_exceptions import IntervalLenght

# Couldn't round the number
from .bis_exceptions import PrecisionNotEnough

from .bis_interval_gen import gen_interval          # Gen interval [a, b]

def bisection(
        function,
        interval: List[Float] = None,
        epsilon: Float = None,
        round_digits: Integer = None,
        max_iter: Integer = None,
        precision: Integer = None,
        rounding_type: Integer = None
        ) -> List[List[Float]]:
    
    """
    return 2d matrix representing a table where each row is the result of this: 
    [n, a, f(a), b, f(b), c, f(c), |f(c)| <= e, f(a) * f(c), sign]

    where:
        a: left interval
        b: right interval
        c: half point
        f(x): function evaluated on point x
        e: epsilon (where to stop)

    https://en.wikipedia.org/wiki/Bisection_method
    """

    if not function.free_symbols:
        raise NoVariableInFunction(
                "Root doesn't exist, due to function not having variables")
    
    if len(function.free_symbols) > 1:
        raise MultipleVariablesInFunction(
                "Function has more than one variable, bisecction only works"
                " " "with 1 variable, the symbols are:"
                " " f"{function.free_symbols}")

    # Bisection works only with 1 symbol.
    symbol = function.free_symbols.pop()

    if not interval: # None or empty interval
        interval = gen_interval(function, symbol, precision=precision)
    
    elif len(interval) != 2:
        raise IntervalLenght(
                "The interval needs exact two values, |a| and |b|")

    a = round(interval[0], precision, round_digits, rounding_type)
    b = round(interval[1], precision, round_digits, rounding_type)

    # Check if root belongs to interval interval [a, b]
    image_a = function.evalf(n=precision, subs={symbol: a}, chop=True)
    image_b = function.evalf(n=precision, subs={symbol: b}, chop=True)

    if (image_a == zoo or image_b == zoo or # Indetermination 1/0
        image_a == nan or image_b == nan or # Indetermination 0/0, oo - oo
        image_a == oo  or image_b == oo  or # Indetermination log_e(0)
        image_a == -oo or image_b == -oo or
        image_a * image_b > 0):             # Interval condition

        raise NotInInterval(f"The root is not on the interval [{a}, {b}]")
    
    table = []
    it = 0
    epsilon = 0 if epsilon is None else epsilon
    epsilon = round(epsilon, precision, round_digits, rounding_type)

    last_c = None
    while it < max_iter: # End condition max iters
        it += 1
        c = (a + b) / Float(2, precision) # Half point
        c = round(c, precision, round_digits, rounding_type)

        # Evaluating the functions
        # Chop is to avoid 1/0 being numerically calculated instead
        # of return zoo
        image_a = function.evalf(n=precision, subs={symbol: a}, chop=True)
        image_b = function.evalf(n=precision, subs={symbol: b}, chop=True)
        image_c = function.evalf(n=precision, subs={symbol: c}, chop=True)
       
        # Half point indetermination
        if (image_c in {zoo, nan, oo, -oo}):
            a, b = interval
            raise NotContinous(f"Function Not continous on interval [{a}, {b}]")
        
        # Round the result of each image
        image_a = round(image_a, precision, round_digits, rounding_type)
        image_b = round(image_b, precision, round_digits, rounding_type)
        image_c = round(image_c, precision, round_digits, rounding_type)

        # End condition epsilon
        if abs(image_c) <= epsilon:

            # Inserting row
            table.append([it, a, image_a, b, image_b, c, image_c, 'YES'])
            break
        
        # Deciding new interval where root belongs
        prod = image_a * image_c
        sign = '-' if prod < 0 else '+'
        prod = round(prod, precision, round_digits, rounding_type)

        # Inserting row
        table.append([it, a, image_a, b, image_b, c, image_c, 'NO', prod, sign])

        # Changing interval where the root belongs
        if sign == '-': # root belongs to [a, c]
            b = c

        else:           # root belongs to [c, b]
            a = c
        
        # End condition x_n = x_n+1
        if last_c == c:
            break
        
        last_c = c
    return table

def round(
        number: Float,
        precision: Integer,
        round_digits: Integer,
        rounding_type):
    
    try:
        from decimal import getcontext, Decimal, InvalidOperation
        getcontext().prec = precision
        number_d = Decimal(str(number))
        exp = Decimal('0.' + '0' * round_digits)
        n = Float(number_d.quantize(exp, rounding=rounding_type), precision)
        return n

    except InvalidOperation:
        raise PrecisionNotEnough(
                f"Precision {precision} not enough to round number {number}"
                " " f"to {round_digits} digits,"
                " " f"try increasing it to {len(str(number))}")

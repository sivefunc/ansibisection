from sympy import oo, zoo, nan, Float

def gen_interval(function, symbol, max_iter=100, precision=15):
    """
    return a tuple indicating the interval [a, b] where the root is
    it starts at 0, 0 and increases to [-1, +1], [-2, +2] and so on
    until the function belongs to the interval.

    if the max iterations is reached it returns [-max_iter, max_iter]
    """

    a, b = Float(0, precision), Float(0, precision)
    iterations = 0
    while iterations < max_iter:
        iterations += 1
        
        # Chop is to avoid 1/0 being numerically calculated instead
        # of return zoo
        image_a = function.evalf(n=precision, subs={symbol: a}, chop=True)
        image_b = function.evalf(n=precision, subs={symbol: b}, chop=True)
        
        # root lies in interval [a, b]
        if ((image_a != zoo or image_b != zoo) and  # Indetermination 1/0
            (image_a != nan or image_b != nan) and  # Ind. 0/0, oo - oo
            (image_a != oo  or image_b != oo)  and
            (image_a != -oo or image_b != -oo) and
            image_a * image_b < 0):                 # Interval condition
            break

        a -= 1
        b += 1
    
    return a, b

# sympy takes a lot of time to load
from sympy import pprint # To print the function
from sympy import plotting #  Make the graph
from tabulate import tabulate

# --------------------------------- #
# Bisection function and exceptions #
# --------------------------------- #
from bisection_method.bis_method import bisection

# root not on interval, image_a * image_b > 0
from bisection_method.bis_exceptions import NotInInterval

# Image of half point (a + b) / 2 is indeterminated aka not continous, e.g 1/0
from bisection_method.bis_exceptions import NotContinous

# Function doesn't contain variable
from bisection_method.bis_exceptions import NoVariableInFunction

# e.g f(x, y) -> x^2 + y^2
from bisection_method.bis_exceptions import MultipleVariablesInFunction

# Interval is not exactly [a, b]
from bisection_method.bis_exceptions import IntervalLenght

# Couldn't round the number
from bisection_method.bis_exceptions import PrecisionNotEnough

# --------#
# Parsing #
# ------- 
# File doesn't contain mandatory argument f(x), e.g: x^2
from data_extraction.exceptions import FunctionNotFound

# Argument on a line can't be converted to a python object, e.g: Float("WORD")
from data_extraction.exceptions import CantConvert

from data_extraction.file_args import file_args # Arguments from file
from data_extraction.term_args import term_args # Arguments from terminal

# Number to a type of rounding of decimal
from RoundingType import type_of_rounding

HEADERS = [
        "N.", "a", "f(a)",
        "b", "f(b)",
        "c", "f(c)", 
        "|f(c)| <= e", "f(a) * f(c)", "sign"]

def main():
    term = term_args()                              # terminal args

    if term.precision <= 0:
        print("Precision can't be less or equal to 0, increase it")
        exit(0)

    file = file_args(term.file, term.precision)     # file args
    
    table = bisection(
            file.function,                          # f(z)
            file.interval,                          # [a, b]
            file.epsilon,                           # Stopping criteria
            file.round_digits,                      # 5 -> 0.00000
            file.max_iter,                          # max number of bis steps.
            term.precision,                         # Digits in calculation
            type_of_rounding(term.rounding_type))   # e.g HALF_UP_EVEN
    
    
    result = tabulate(
        table,                              # The numbers on each iter.
        HEADERS,                            # The title
        tablefmt="simple_grid",             # rectangular grid
        floatfmt=f".{file.round_digits}f")  # 5 -> 0.00000
    
    pprint(file.function)                   # Shows the function
    print(result)
    
    # Generates the graph
    if term.graph:
        c, image = table[-1][5], table[-1][6]
        plotting.plot(
                file.function,
                markers=[{'args': [[c], [image], "o"]}],
                title=file.function)

if __name__ == '__main__':
    try:
        main()
    
    # Exceptions related to file args, term args and bisection method.
    except (
            FileNotFoundError,
            CantConvert,            # Data in file can't be converted.
            FunctionNotFound,       # Mandatory argument is not there
            NotInInterval,          # Root is not on the interval
            NotContinous,           # Function indeterminated at half point
            NoVariableInFunction,   # f() : 5 + 3^2
            IntervalLenght,         # Interval is not exactly [a, b]
            PrecisionNotEnough,     # Can't round the number
            MultipleVariablesInFunction) as error: # f(x, y) : x^2 + y^2

        print(error)

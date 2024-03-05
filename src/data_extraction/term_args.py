import argparse
from defaults import TOTAL_PRECISION, ROUNDING_TYPES, ROUNDING_TYPE

def term_args():
    parser = argparse.ArgumentParser(
            prog="AnsiBisection",
            formatter_class=argparse.RawTextHelpFormatter,
            usage='%(prog)s [options]',
            description="Root of single variable function using bisection method")

    parser.add_argument(
            '-v','--version',
            action='version',
            version="""
%(prog)s v1.0.0
Copyright (C) 2024 Sivefunc
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by a human""")

    parser.add_argument(
            'file',
            type=str,
            help='path of file containing function and optional arguments',
            metavar="file")

    parser.add_argument(
            "-rt", '--rounding_type', 
            type=int,
            help=f"""rounding modes:
|0 -> ROUND_CEILING|
|1 -> ROUND_DOWN|
|2 -> ROUND_FLOOR|
|3 -> ROUND_HALF_DOWN|
|4 -> ROUND_HALF_EVEN|
|5 -> ROUND_HALF_UP|
|6 -> ROUND_UP|
|7 -> ROUND_05UP|
(default: {ROUNDING_TYPE})
""",
            default=ROUNDING_TYPE,
            choices=ROUNDING_TYPES,
            metavar='')

    parser.add_argument(
            "-p", '--precision', 
            type=int,
            help='Number of digits when doing calculations,'
            ' ' f'(default: {TOTAL_PRECISION})',
            default=TOTAL_PRECISION,
            metavar='')

    parser.add_argument(
            '-g', '--graph',
            action="store_true",
            help="Graph f(x) onto a cartesian plane (show's also root)")

    parser.add_argument(
            '-n','--notation',
            action='version',
            help="Shows how to format the file, default values and exit",
            version="""
Comments
Written using double quotes ' " '
Everything in pair of "" gets ignored, if pair is not found delete until EOL
e.g: " This is a comment "
-------------------------------------------------------------------------------
Arrows (Optional)
Written on the form '->'
These are made to indicate the value of an argument
e.g: argument -> value
-------------------------------------------------------------------------------
Function (Single variable) Mandatory argument
Written using this:
Exponentiaton   -> a^b, a**b
Multiplication  -> a * b
Division        -> a / b
Subtraction     -> a - b
Summation       -> a + b
Parenthesis to group things
functions like cos, sine, log10, ln and stuff like pi and e
e.g: function -> log(z^2) - cos(z^2 * 2) + z * 5
-------------------------------------------------------------------------------
Interval [Float, Float] (Optional argument)
Written using closed brackets [ and ]
If no interval is given a interval is generated
e.g: interval -> [123.45, 678.90]
-------------------------------------------------------------------------------
Epsilon (Optional argument) Stopping criteria -> Float
If no epsilon is given it will stop until the number of max iter is reached
e.g: epsilon -> 0.0100
-------------------------------------------------------------------------------
Round_Digits (Optional argument) integer
Default: 5
e.g round_digits -> 12
-------------------------------------------------------------------------------
iterations Stopping criteria (Optional argument) integer
Default: 100
e.g iterations -> 15
""")
    args = parser.parse_args()
    return args

# Conversion of the function mandatory argument to a sympy object
from sympy import sympify, SympifyError

# Conversion of other arguments to sympy objects
from sympy import Float, Integer

# File doesn't contain mandatory argument f(x), e.g: x^2
from .exceptions import FunctionNotFound

# Argument on a line can't be converted to a python object, e.g: Float("WORD")
from .exceptions import CantConvert
from types import SimpleNamespace

from defaults import EPSILON, INTERVAL, MAX_ITER, ROUND_DIGITS, FUNCTION

def delete_comments(line: str):
    """
    return a str that doesn't contain the characters between double quote
    symbols, if pair is not found it deletes until end of line.
    """

    new_line = ""
    comment_found = False
    for ch in line:
        if ch == '"': # end of pair or start of new pair.
            comment_found = False if comment_found else True

        elif not comment_found:
            new_line += ch
    
    return new_line

def file_args(file_path: str, precision):
    """
    return a namespace that represent the conversion of file
    to the corresponding:

    1. polynomial
    2. interval
    3. epsilon
    4. precision
    5. max iter
    
    It ignores the rest of the lines after the 5 arguments are given. 
    The arguments not given get set to None

    data = SimpleNamespace(
        function=val, interval=val, epsilon=val, precision=val, max_iter=val)
    """

    with open(file_path, 'r') as f:
        lines = []
        for line in f.readlines():
            line = delete_comments(line.strip('\n').replace('->', '').strip())
            if line:
                lines.append(line)

    return data_conversion(lines, precision)
    
def data_conversion(lines, precision) -> tuple:
    """
    Convert each line to the corresponding argument
    """

    # Converting first line (polynomial) to a sympy object
    data = SimpleNamespace(
            function=FUNCTION, 
            interval=INTERVAL,
            epsilon=EPSILON,
            round_digits=ROUND_DIGITS,
            max_iter=MAX_ITER)
    
    try:
        for idx, line in enumerate(lines):
            argument = ""
            for ch in line:
                argument += ch.lower()
                if argument == 'function':
                    info = lines[idx][len(argument):].strip()
                    data.function = sympify(info)
                    break

                elif argument == 'interval':
                    info = lines[idx][len(argument):].strip().replace(
                        '[', ' ').replace(']', ' ').replace(',', ' ').split()

                    data.interval = [Float(v, precision) for v in info]
                    break

                elif argument == 'epsilon':
                    info = lines[idx][len(argument):].strip()
                    data.epsilon = Float(info, precision)
                    break

                elif argument == 'round_digits':
                    info = lines[idx][len(argument):].strip()
                    data.round_digits = Integer(info)
                    break

                elif argument == 'iterations':
                    info = lines[idx][len(argument):].strip()
                    data.max_iter = Integer(info)
                    break

    except SympifyError:
        raise CantConvert(
                f"The function argument |{lines[idx]}| couldn't be converted to"
                " " "a python object, bad formatting?\n"
                "type -n or --notation to know how to format")

    except ValueError:
        raise CantConvert(
                f"The {argument} argument |{lines[idx]}| located on line"
                " " "couldn't be converted to a python object, bad"
                " " "formatting?\n"
                "type -n or --notation to know how to format")   
    
    if data.function is None:
        raise FunctionNotFound("Mandatory argument function not found on file")

    return data 

class NotInInterval(Exception):
    """ 
    Raise when the root of polynomial is not on the interval [a, b]
    """

class NotContinous(Exception):
    """ 
    Raise when the function is not continous on a interval [a, b]
    """

class NoVariableInFunction(Exception):
    """ 
    Raise when the function doesn't contain variable
    """

class MultipleVariablesInFunction(Exception):
    """
    Raise when the function is multivariable
    """

class MultipleVariablesInFunction(Exception):
    """
    Raise when the function is multivariable
    """

class IntervalLenght(Exception):
    """
    Raise when the interval doesn't contain exactly [a, b]
    """

class PrecisionNotEnough(Exception):
    """
    Raise when the precision is not enough when rounding or calculating
    """

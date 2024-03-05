class FunctionNotFound(Exception):
    """
    Raise when output of preprocessed file is empty and that means that the
    mandatory function argument is not available.
    """

class CantConvert(Exception):
    """
    Raise when the line can't be converted to a python object.
    probably it's because the line is not correctly formatted.
    """

# https://docs.python.org/3/library/decimal.html#rounding-modes
from decimal import (
        ROUND_CEILING, ROUND_DOWN, ROUND_FLOOR, ROUND_HALF_DOWN,
        ROUND_HALF_EVEN, ROUND_HALF_UP, ROUND_UP, ROUND_05UP)

rounding = {
        0: ROUND_CEILING,
        1: ROUND_DOWN,
        2: ROUND_FLOOR,
        3: ROUND_HALF_DOWN,
        4: ROUND_HALF_EVEN,
        5: ROUND_HALF_UP,
        6: ROUND_UP,
        7: ROUND_05UP
        }

def type_of_rounding(rounding_type: int):
    return rounding[rounding_type]

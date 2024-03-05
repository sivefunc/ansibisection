# ------------- #
# Terminal args #
# ------------- #
TOTAL_PRECISION = 32            # N of digits when doing calculations

# Methods of rounding from decimal module
ROUNDING_TYPES = [
        0, # ROUND_CEILING
        1, # ROUND_DOWN
        2, # ROUND_FLOOR
        3, # ROUND_HALF_DOWN
        4, # ROUND_HALF_EVEN
        5, # ROUND_HALF_UP
        6, # ROUND_UP
        7, # ROUND_05UP
        ]
ROUNDING_TYPE = 5               # Default roudning type

# --------- #
# File args #
# --------- #
FUNCTION = None
EPSILON = None                  # Stopping criteria
                                # None = x_n = x_n+1

INTERVAL = None                 # Interval [a, b] where the root belongs
                                # None = gen interval

ROUND_DIGITS = 5                # 0.00000 -> Result after each operation
MAX_ITER = 100                  # Stop bisection at this N. of Iterations

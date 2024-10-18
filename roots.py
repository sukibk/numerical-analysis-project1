import math


def f(x):
    # Function f(x) = tan(pi * x) - x - 6
    return math.tan(math.pi * x) - x - 6


def find_root_interval(a_start, b_start, step=0.1, max_iters=1000):
    """
    Find an interval [a, b] where the function f changes sign.

    Parameters:
    a_start, b_start: initial guesses for a and b
    step: increment step size for finding the interval
    max_iters: maximum number of iterations to avoid infinite loops

    Returns:
    Tuple of (a, b) where f(a) and f(b) have opposite signs, or None if not found
    """
    a, b = a_start, b_start
    for _ in range(max_iters):
        fa = f(a)
        fb = f(b)

        if fa * fb < 0:  # Function changes sign, meaning root exists in [a, b]
            return a, b

        # Move the points to search further if no sign change found
        a -= step
        b += step

    return None


# Start with initial guesses
a_start = 0.1
b_start = 0.2

# Find the interval
interval = find_root_interval(a_start, b_start)

if interval:
    print(f"Root is in the interval: {interval}")
else:
    print("No root found within the given range.")

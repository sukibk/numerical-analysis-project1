import math

def func(x):
    """ Define the function to find the root for. """
    return math.tan(math.pi * x) - x - 6


def sign(val):
    """ Return the sign of the given value. """
    return -1 if val < 0 else 1


def bisection_algorithm(a, b, Nmax, epsilon):
    """
    Bisection method to find the root of a function within a given interval [a, b].

    Parameters:
    a : float
        Left endpoint of the interval.
    b : float
        Right endpoint of the interval.
    Nmax : int
        Maximum number of iterations.
    epsilon : float
        Convergence tolerance.

    Returns:
    The root if found within tolerance, otherwise a message indicating failure.
    """

    # STEP 1: save sfa = sign(f(a))
    sfa = sign(func(a))

    # STEP 2: For i from 1 to Nmax do
    for i in range(1, Nmax + 1):
        # STEP 3: p = a + (b - a) / 2
        p = a + (b - a) / 2

        # STEP 4: if (b - a) < 2 * epsilon then OUTPUT p
        if (b - a) < 2 * epsilon:
            print(f"The root is approximately: {p} (converged at iteration {i})")
            return p

        # STEP 5: save sfp = sign(f(p))
        sfp = sign(func(p))

        # Output the current iteration and p value
        print(f"Iteration {i}. P value is: {p}")

        # STEP 6: if (sfa * sfp < 0) then
        if sfa * sfp < 0:
            # assign the value of p to b
            b = p
        else:
            # assign the value of p to a
            a = p
            # assign the value of sfp to sfa
            sfa = sfp

    # STEP 7: OUTPUT a message that the maximum number of iterations has been exceeded
    print("The maximum number of iterations has been exceeded without convergence")
    return None


def get_user_input_bisection():
    """
    Function to get user input for the interval and iteration parameters.

    Returns:
    a : float
        Left endpoint of the interval.
    b : float
        Right endpoint of the interval.
    Nmax : int
        Maximum number of iterations.
    epsilon : float
        Convergence tolerance.
    """
    a = float(input("Enter the left endpoint of the interval (a): "))  # Left endpoint of interval
    b = float(input("Enter the right endpoint of the interval (b): "))  # Right endpoint of interval
    Nmax = int(input("Enter the maximum number of iterations (Nmax): "))  # Maximum number of iterations
    epsilon = 1e-7  # Convergence tolerance (fixed)
    return a, b, Nmax, epsilon


def execute_bisection_algorithm():
    """
    Function to execute the bisection method with user inputs.
    """
    a, b, Nmax, epsilon = get_user_input_bisection()

    # Running the bisection algorithm
    bisection_algorithm(a, b, Nmax, epsilon)

# You can now export all functions from this file to use them elsewhere

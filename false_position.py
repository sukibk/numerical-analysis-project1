import math


def f(x):
    """
    Define the function for which we are finding the root.
    """
    return x ** 3 + 2 * x ** 2 - 3 * x - 1


def false_position(f, a, b, tol, Nmax):
    """
    False position method to find the root of a function.

    Parameters:
    f : function
        The function whose root is being determined.
    a : float
        Left endpoint of the interval.
    b : float
        Right endpoint of the interval.
    tol : float
        Convergence tolerance.
    Nmax : int
        Maximum number of iterations.

    Returns:
    Root and number of iterations if convergence is achieved within tolerance, otherwise raises an error.
    """
    # Initial function values
    fa = f(a)
    fb = f(b)

    # Check if the function values at a and b have opposite signs
    if fa * fb > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")

    p_older = b
    p_old = b

    for i in range(1, Nmax + 1):
        # Calculate the false position point
        p = b - fb * (b - a) / (fb - fa)
        print(f"Iteration {i}: p = {p}")

        # Check stopping condition after the second iteration
        if i > 2:
            λ = (p - p_old) / (p_old - p_older)
            err_est = abs(λ * (p - p_old) / (λ - 1))
            print(f"Error estimate = {err_est}")
            if err_est < tol:
                print(f"Converged to root: {p} after {i} iterations with error: {err_est}")
                return p, i  # Return the root and number of iterations

        # Save the function value at p
        fp = f(p)

        # Check which side of the interval contains the root
        if fa * fp < 0:
            b = p
            fb = fp
        else:
            a = p
            fa = fp

        # Update old values for the next iteration
        p_older = p_old
        p_old = p

    raise RuntimeError("Maximum number of iterations exceeded")


def get_user_input():
    """
    Function to get user input for the interval and iteration parameters.

    Returns:
    a : float
        Left endpoint of the interval.
    b : float
        Right endpoint of the interval.
    Nmax : int
        Maximum number of iterations.
    tol : float
        Convergence tolerance.
    """
    a = float(input("Enter the left endpoint of the interval (a): "))  # Left endpoint of interval
    b = float(input("Enter the right endpoint of the interval (b): "))  # Right endpoint of interval
    Nmax = int(input("Enter the maximum number of iterations (Nmax): "))  # Maximum number of iterations
    tol = 1e-7  # Convergence tolerance (fixed)
    return a, b, Nmax, tol


def execute_false_position():
    """
    Function to execute the false position method with user inputs.
    """
    a, b, Nmax, tol = get_user_input()

    # Try to find the root using the false position method
    try:
        root, iterations = false_position(f, a, b, tol, Nmax)
        print(f"Root found at x = {root}, after {iterations} iterations")
    except RuntimeError as e:
        print(e)
    except ValueError as ve:
        print(ve)

# Export the functions for use in another file

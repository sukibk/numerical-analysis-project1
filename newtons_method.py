import math


def newton_method(f, df, x0, epsilon, Nmax):
    """
    Newton's method to find the root of a function.

    Parameters:
    f       - Function whose root is to be found.
    df      - Derivative of the function.
    x0      - Initial approximation (guess).
    epsilon - Convergence tolerance.
    Nmax    - Maximum number of iterations.

    Returns:
    The root of the function if found within tolerance, otherwise a message indicating failure.
    """
    print(f"Initial guess: {x0}")

    for i in range(Nmax):
        # Calculate the next approximation using Newton's method formula
        try:
            x1 = x0 - f(x0) / df(x0)
        except ZeroDivisionError:
            return "Error: Division by zero in derivative calculation."

        # Calculate the error (difference between current and previous approximation)
        error = abs(x1 - x0)

        # Output the current iteration, guess, and error
        print(f"Iteration {i + 1}: Guess = {x1}, Error = {error}")

        # Check for convergence
        if error < epsilon:
            print(f"Converged to root: {x1} after {i + 1} iterations with error: {error}")
            return x1

        # Update the current approximation for the next iteration
        x0 = x1

    # If the loop completes without finding the root, output a message
    print("Maximum number of iterations has been exceeded without convergence.")
    return None


def get_user_input_newton():
    """
    Function to get user input for Newton's method.

    Returns:
    x0 : float
        Initial guess.
    Nmax : int
        Maximum number of iterations.
    epsilon : float
        Convergence tolerance.
    """
    x0 = float(input("Enter the initial guess (x0): "))  # Take x0 from user
    Nmax = int(input("Enter the maximum number of iterations (Nmax): "))  # Take Nmax from user
    epsilon = 1e-7  # Tolerance for convergence (fixed)
    return x0, Nmax, epsilon


def execute_newton_method():
    """
    Function to execute Newton's method with user input.
    """

    # Define the function and its derivative
    def f(x):
        return math.tan(math.pi * x) - x - 6  # Example function

    def df(x):
        return math.pi * (1 / math.cos(math.pi * x) ** 2) - 1  # Derivative of the function

    # Get input values from the user
    x0, Nmax, epsilon = get_user_input_newton()

    # Finding the root using Newton's method
    root = newton_method(f, df, x0, epsilon, Nmax)

    # Output the result
    if root is not None:
        print(f"Final root: {root}")

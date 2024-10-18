import math

def newton_method_with_acceleration(f, df, x0, epsilon, Nmax):
    """
    Newton's method with Aitken's Δ² acceleration to find the root of a function.

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

    x_old = x0  # p_n
    x_older = None  # p_(n-1), we don't have it yet

    for i in range(Nmax):
        # Calculate the next approximation using Newton's method formula
        try:
            x_new = x_old - f(x_old) / df(x_old)
        except ZeroDivisionError:
            return "Error: Division by zero in derivative calculation."

        # Apply Aitken's Δ² acceleration if we have at least 3 estimates
        if i > 1:
            denominator = x_new - 2 * x_old + x_older
            if denominator != 0:  # Avoid division by zero
                x_acc = x_old - ((x_new - x_old) ** 2) / denominator
                x_new = x_acc  # Use the accelerated value
                print(f"Iteration {i + 1}: Accelerated Guess = {x_new}")

        # Calculate the error (difference between current and previous approximation)
        error = abs(x_new - x_old)

        # Output the current iteration, guess, and error
        print(f"Iteration {i + 1}: Guess = {x_new}, Error = {error}")

        # Check for convergence
        if error < epsilon:
            print(f"Converged to root: {x_new} after {i + 1} iterations with error: {error}")
            return x_new

        # Update the approximations for the next iteration
        x_older = x_old
        x_old = x_new

    # If the loop completes without finding the root, output a message
    print("Maximum number of iterations has been exceeded without convergence.")
    return None


def get_user_input_newton():
    """
    Function to get user input for the initial guess and iteration parameters.

    Returns:
    x0       - Initial guess for Newton's method.
    Nmax     - Maximum number of iterations.
    epsilon  - Convergence tolerance (fixed).
    """
    x0 = float(input("Enter the initial guess (x0): "))  # Take x0 from user
    Nmax = int(input("Enter the maximum number of iterations (Nmax): "))  # Take Nmax from user
    epsilon = 1e-7  # Tolerance for convergence (fixed)
    return x0, Nmax, epsilon


def execute_newton_with_acceleration():
    """
    Function to execute Newton's method with Aitken's acceleration using user input.
    """
    # Define the function and its derivative
    def f(x):
        return math.tan(math.pi * x) - x - 6  # The given function

    def df(x):
        return math.pi * (1 / math.cos(math.pi * x) ** 2) - 1  # Derivative of the function

    # Get user input
    x0, Nmax, epsilon = get_user_input_newton()

    # Execute the Newton method with Aitken's acceleration
    root = newton_method_with_acceleration(f, df, x0, epsilon, Nmax)
    if root is not None:
        print(f"Final root: {root}")

# Export all necessary functions for use in another file

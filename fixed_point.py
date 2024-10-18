import math

def fixed_point_iteration(g, x0, epsilon, Nmax):
    """
    Fixed-point iteration method to find the root of a function.

    Parameters:
    g : function
        Iteration function g(x).
    x0 : float
        Initial approximation.
    epsilon : float
        Convergence tolerance.
    Nmax : int
        Maximum number of iterations.

    Returns:
    The root of the function if found within tolerance, otherwise a message indicating failure.
    """

    x1 = x0  # Step 1: Initialize x1 = x0
    print(f"Initial guess: {x0}")

    for i in range(1, Nmax + 1):  # Step 2: Loop for i from 1 to Nmax
        x2 = g(x1)  # Step 3: Set x2 = g(x1)
        print(f"Iteration {i}: Guess = {x2}")

        # If we are on the third iteration or beyond, calculate error estimate
        if i > 2:  # Step 4: If i > 2
            # Calculate gp = (x2 - x1) / (x1 - x0)
            try:
                gp = (x2 - x1) / (x1 - x0)  # Ensure we handle division by zero safely
                err_est = abs(gp * (x2 - x1) / (gp - 1))  # Error estimate calculation
            except ZeroDivisionError:
                return "Error: Division by zero occurred in error estimate."

            print(f"Error estimate = {err_est}")  # Output error estimate for the current iteration

            # Check if the error estimate is below the convergence tolerance
            if err_est < epsilon:  # If error is less than epsilon, we have converged
                print(f"Converged to root: {x2} after {i} iterations with error: {err_est}")
                return x2

        # Step 5: Update x0 and x1 for the next iteration
        x0 = x1
        x1 = x2

    # If the method does not converge within the maximum number of iterations
    return "Maximum number of iterations exceeded"


def get_user_input_fixed_point():
    """
    Function to get user input for the initial guess and iteration parameters.

    Returns:
    x0 : float
        Initial guess for the fixed-point iteration.
    Nmax : int
        Maximum number of iterations.
    epsilon : float
        Convergence tolerance (fixed).
    """
    x0 = float(input("Enter the initial guess (x0): "))  # Take x0 from user
    Nmax = int(input("Enter the maximum number of iterations (Nmax): "))  # Take Nmax from user
    epsilon = 1e-7  # Convergence tolerance (fixed)
    return x0, Nmax, epsilon


def execute_fixed_point_iteration():
    """
    Function to execute the fixed-point iteration with user inputs.
    """
    # Define the iteration function g(x)
    def g(x):
        # Transformed function for fixed-point iteration: g(x) = tan(pi * x) - 6
        return math.tan(math.pi * x) - 6

    # Get user input
    x0, Nmax, epsilon = get_user_input_fixed_point()

    # Perform fixed-point iteration
    result = fixed_point_iteration(g, x0, epsilon, Nmax)

    # Output the final result
    if result:
        print(f"Final result: {result}")

# All functions are now ready to be imported and used in other scripts

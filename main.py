from fixed_point import execute_fixed_point_iteration
from bisection import execute_bisection_algorithm
from false_position import execute_false_position
from newtons_method import execute_newton_method
from newtons_method_acceleration import execute_newton_with_acceleration


def main():
    """ Main function to choose and run methods. """
    while True:
        print("\nSelect a method to execute:")
        print("1. Fixed-Point Iteration")
        print("2. Bisection Method")
        print("3. False Position Method")
        print("4. Newton's Method")
        print("5. Newton's Method with Acceleration")
        print("6. Quit")

        choice = input("Enter your choice (1, 2, 3, 4, 5, or 6): ")

        if choice == "1":
            print("\nYou selected Fixed-Point Iteration.")
            execute_fixed_point_iteration()

        elif choice == "2":
            print("\nYou selected Bisection Method.")
            execute_bisection_algorithm()

        elif choice == "3":
            print("\nYou selected False Position Method.")
            execute_false_position()

        elif choice == "4":
            print("\nYou selected Newton's Method.")
            execute_newton_method()

        elif choice == "5":
            print("\nYou selected Newton's Method with Acceleration.")
            execute_newton_with_acceleration()

        elif choice == "6":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the main function
if __name__ == "__main__":
    main()

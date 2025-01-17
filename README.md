# Root-Finding Algorithms Comparison Project

## 📚 Overview
This project implements and compares various numerical methods for finding the roots of a given function. It includes the following algorithms:

- **Fixed-Point Iteration**
- **Bisection Method**
- **False Position Method**
- **Newton's Method**
- **Newton's Method with Aitken's Acceleration**

Each algorithm is implemented in a separate Python file, and the project provides an interactive menu that allows the user to choose which method to execute. The methods are tested with a sample function, and results are compared based on convergence speed, number of iterations, and accuracy.

---

## 📁 Project Structure

### Files
- **`main.py`**: The main driver file that offers a menu for selecting and running each algorithm.
- **`fixed_point.py`**: Contains the implementation of the Fixed-Point Iteration method and its input/execution function.
- **`bisection.py`**: Contains the implementation of the Bisection Method and its input/execution function.
- **`false_position.py`**: Contains the implementation of the False Position Method and its input/execution function.
- **`newtons_method.py`**: Contains the implementation of Newton's Method and its input/execution function.
- **`newtons_method_acceleration.py`**: Contains the implementation of Newton's Method with Aitken's Acceleration and its input/execution function.

### Results
Each method outputs the following data during execution:
- Number of iterations required for convergence
- Approximate root value found
- Error estimates for each iteration
- Number of function evaluations

The **Newton’s Method with Aitken’s Acceleration** typically provides the fastest and most accurate results but requires both the function and its derivative. The **Bisection** and **False Position Methods** are reliable but slower in comparison.

---

## 🚀 How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/sukibk/numerical-analysis-project1
   cd numerical-analysis-project1
   ```

2. Run the `main.py` file:
   ```bash
   python main.py
   ```

3. Follow the interactive menu to select the algorithm you want to run:
   - Choose an algorithm.
   - Provide the necessary inputs (initial guesses, intervals, etc.).
   - View the results for the selected method.

---

## 📝 License
This project is licensed under the MIT License.

---

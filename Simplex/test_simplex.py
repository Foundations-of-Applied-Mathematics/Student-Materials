"""Unit testing file for the Simplex lab"""

import simplex
import numpy as np

def test_simplex():
    """
    Write at least one unit test for problem 5, the simplex solver.
    """
    raise NotImplementedError("No code written for problem 5 unit test!!")

def test_simplex_example():
    # Sets up the values for the simplex problem.
    c = np.array([-3, -2])
    b = np.array([2, 5, 7])
    A = np.array([[1, -1], [3, 1], [4, 3]])

    # Runs the simplex solver.
    solver = simplex.SimplexSolver(c, A, b)
    sol = solver.solve()

    # Checks if it returned the correct value
    assert sol[0] == -5.2, "Incorrect result from the simplex method"

"""Unit testing file for CVXPY Intro lab"""


import cvxpy_intro
import numpy as np

def test_prob5():
    """
    Write at least one unit test for problem 5.
    """
    raise NotImplementedError("No code written for problem 5 unit test!!")

def test_l1Min():
    # Sets up the matrix and vector
    A = np.array([[1, 2, 1, 1],
                 [0, 3, -2, -1]])
    b = np.array([7, 4])

    # Runs the l1Min function on the matrix and vector
    x, ans = cvxpy_intro.l1Min(A, b)
    
    # Checks for the correct vector and minimum value
    assert np.linalg.norm(x - np.array([0.0, 2.571, 1.857, 0.0])) <= 1e-3, "Returned the wrong minimizer"
    assert abs(ans - 4.429) <= 1e-3, "Returned the wrong mimimum"
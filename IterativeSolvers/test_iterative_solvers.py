"""Unit testing file for Iterative Solvers lab"""


import iterative_solvers
import numpy as np

def test_gauss_seidel_sparse():
    """
    Write at least one unit test to test your function from problem 4,
    the Guass-Seidel method  sparse matrices.
    """
    raise NotImplementedError("No code written for problem 4 unit test!!")

def test_jacobi():
    # Runs the test for different values of n.
    for n in range(1, 15):
        # Sets up the matrix and the vector.
        b = np.random.random(n)
        A = iterative_solvers.diag_dom(n)

        # Finds the vector using the function.
        x = iterative_solvers.jacobi(A, b)

        # Makes sure the correct vector was found.
        assert np.allclose(A @ x, b), f"Incorrect vector found for n = {n}"
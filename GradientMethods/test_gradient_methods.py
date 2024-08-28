"""Unit testing file for Gradient Descent Methods lab"""

import gradient_methods
import numpy as np

def test_nonlinear_conjugate_gradient():
    """
    Write at least one unit test for problem 3, the nonlinear conjugate gradient function.
    """
    raise NotImplementedError("No code written for problem 3 unit test!!")

def test_conjugate_gradient():
    # Tests different sized matrices to see if they converge
    for n in range(1, 5):
        A = np.random.random((n, n))
        b = np.random.random(n)
        Q = A.T @ A
        x, conv, k = gradient_methods.conjugate_gradient(Q, b, np.random.random(n))
        if conv:
            assert np.allclose(Q @ x, b), "Incorrect vector found"
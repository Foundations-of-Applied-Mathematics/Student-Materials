"""Unit testing file for Newton's Method Lab"""


import newtons_method
import pytest
from math import isclose

def test_newton():
    """
    Write at least one unit test for problem 5,
    Newton's method for vector-valued functions.
    """
    raise NotImplementedError("No code written for problem 5 unit test!!")

def test_prob2():
    """ Test cases for problem 2. """
    assert isclose(newtons_method.prob2(30, 20, 2000, 8000), 0.03878, abs_tol=1e-5), "Incorrect r for N1=30, N2=20, P1=2000, P2=8000"
    assert isclose(newtons_method.prob2(10, 10, 20, 100), 0.17462, abs_tol=1e-5), "Incorrect r for N1=10, N2=10, P1=20, P2=100"
    assert isclose(newtons_method.prob2(20, 40, 400, 2000), 0.09238, abs_tol=1e-5), "Incorrect r for N1=20, N2=40, P1=400, P2=2000"
    
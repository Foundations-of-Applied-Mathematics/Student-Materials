"""Unit testing file for linear_systems.py"""

import numpy as np
import numpy.linalg as la
import linear_systems

def valid_matrix(A):
    """Helper function to determine if a matrix won't require row swaps"""
    n = len(A)
    for column in range(1, n-1):
        for row in range(column):
            if np.allclose((A[column, :column+1]/A[column, 0]), (A[row, :column+1]/A[row, 0])):
                return False
    return True

def test_ref():
    """Unit Test for problem 1 of linear systems"""
    A = np.eye(4)
    assert np.allclose(linear_systems.ref(A), A) == True, 'failed on a square matrix'
   
    while True:
        B = np.random.randint(3, 9, size=(5, 5))
        if la.det(B) != 0 and valid_matrix(B):
            break

    val = linear_systems.ref(B)
    assert np.allclose(np.diag(np.diag(val)), np.tril(val)) == True, 'random non identity nxn matrix failed test'


def test_lu():
    """Unit Test for problem 2 of linear systems"""
    A = np.eye(4)
    L, U = linear_systems.lu(A)
    assert np.allclose(L, A) == True, 'failed lower triangular matrix'
    assert np.allclose(U, A) == True, 'failed upper triangular matrix'
    
    B = np.array([[6, 6, 5, 8, 4],
                  [6, 5, 4, 3, 8],
                  [4, 3, 4, 8, 5],
                  [4, 5, 3, 5, 7],
                  [4, 7, 6, 6, 4]])

    L, U = linear_systems.lu(B)
    assert np.allclose(B, L@U) == True, 'incorrect LU decomposition matrix'

def test_solve():
    """Unit Test for Problem 3 of linear systems"""
    
    raise NotImplementedError('No Unit Test written for Solve Function')
    #input your own unit test here 

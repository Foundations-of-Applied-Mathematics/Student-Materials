"""Unit testing file for Conditioning and Stability Lab"""

import conditioning_stability
import numpy as np
import scipy.linalg as sla
from math import isclose

def test_matrix_cond():
    """
    Write at least one unit test for problem 1,
    testing conditioning numbers for non-orthonormal matrices.
    """
    raise NotImplementedError("No code written for problem 1 unit test!!")

def test_ortho_matrix_cond():
    # Sets up the orthonormal matrices for testing
    A = np.array([[1, 0], [0, 1]])
    Q, R = sla.qr(np.random.random((4, 4)))
    
    # Checks to make sure orthonormal matrices give a conditioning number of 1
    assert isclose(conditioning_stability.matrix_cond(A), 1), "Wrong conditioning number for identity matrix"
    assert isclose(conditioning_stability.matrix_cond(Q), 1), "Wrong conditioning number for random matrix"
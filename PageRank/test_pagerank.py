"""Unit testing file for the PageRank lab"""


import pagerank
import numpy as np

def test_prob2():
    """
    Write unit tests to test the eigensolve and itersolve methods for problem 2.
    """
    raise NotImplementedError("No code written for problem 2 unit test!!")

def test_linsolve():
    # Sets up the matrix in the example.
    A = np.array([[0, 0, 0, 0],
                  [1, 0, 1, 0],
                  [1, 0, 0, 1],
                  [1, 0, 1, 0]])
    
    # Sets up the class to be used for the pagerank
    dg1 = pagerank.DiGraph(A, labels=["a", "b", "c", "d"])

    # Finds the p vector.
    p = np.array(list(dg1.linsolve().values()))

    # Checks that the p vector sums to 1 and has the correct values.
    assert np.isclose(p.sum(), 1), "p vector doesn't sum to 1"
    assert np.allclose(p, np.array([0.095758635, 0.274158285, 0.355924792, 0.274158285])), "p vector returns the incorrect values"

"""Unit testing file for Nearest Neighbors"""


import nearest_neighbor
import pytest
import numpy as np


#Perform unit tests for problem 2
def test_KDTNode():
    """
    Write at least one unit test for problem 2, the KDTNode initializer.
    """
    raise NotImplementedError("No code written for problem 2 unit test!!")

#Provided unit tests for problem 3
@pytest.fixture
def set_up_tree():
    tree1 = nearest_neighbor.KDT()
    tree2 = nearest_neighbor.KDT()
    tree3 = nearest_neighbor.KDT()
    
    tree1.insert(np.array([5, 5]))
    
    tree2.insert(np.array([5, 5]))
    tree2.insert(np.array([3, 2]))
    
    tree3.insert(np.array([3, 1, 4]))
    tree3.insert(np.array([1, 2, 7]))
    tree3.insert(np.array([2, 4, 5]))
    return tree1, tree2, tree3

def test_KDT_insert(set_up_tree):
    tree1, tree2, tree3 = set_up_tree
    
    #Makes sure that the root was inserted correctly
    assert (tree1.root.value == np.array([5, 5])).all(), "Incorrect root"
    assert (tree2.root.value == np.array([5, 5])).all(), "Incorrect root"
    assert (tree3.root.value == np.array([3, 1, 4])).all(), "Incorrect root"
    
    #Makes sure that the nodes were inserted into the correct places
    assert tree1.root.left == None, "Incorrect insert"
    assert (tree2.root.left.value == np.array([3, 2])).all(), "Incorrect insert"
    assert tree3.root.right == None, "Incorrect insert"
    
    #Checks if it raises an error if you try to insert with a node of the incorrect size
    pytest.raises(ValueError, tree1.insert, np.array([1, 2, 3])), "Didn't raise exception for incorrect size"
    pytest.raises(ValueError, tree2.insert, np.array([1, 2, 3])), "Didn't raise exception for incorrect size"
    pytest.raises(ValueError, tree3.insert, np.array([1, 2])), "Didn't raise exception for incorrect size"
    
    #Makes sure the pivot number is getting defined correctly
    assert tree1.root.pivot == 0, "Incorrect pivot number"
    assert tree2.root.left.pivot == 1, "Incorrect pivot number"
    assert tree3.root.left.right.pivot == 2, "Incorrect pivot number"
    
    #Makes sure it raises an error if you insert a duplicate node
    pytest.raises(ValueError, tree1.insert, np.array([5, 5])), "Didn't raise exception for duplicate node"
    pytest.raises(ValueError, tree2.insert, np.array([3, 2])), "Didn't raise exception for duplicate node"
    pytest.raises(ValueError, tree3.insert, np.array([2, 4, 5])), "Didn't raise exception for duplicate node"
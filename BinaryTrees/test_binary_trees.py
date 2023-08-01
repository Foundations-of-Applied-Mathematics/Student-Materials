"""Unit testing file for binary_trees.py"""

import binary_trees
import pytest

@pytest.fixture #pytest fixture to help in the construction of a tree
def build_the_tree():
    tree_1 = binary_trees.BST()
    for i in [4,3,8,1,2,9,23,6,5,7]:
        tree_1.insert(i)
    return tree_1
    

def test_insert(build_the_tree):
    """Unit test problem 2, creating an insert method for your BST class"""
    
    tree1 = build_the_tree
    assert tree1.root.value == 4, "root inserted correctly"

    parent = tree1.root
    assert parent.right.value == 8, "right child of root inserted incorrectly"
    assert parent.left.value == 3, "left child of root inserted incorrectly"

    val1 = parent.left
    assert val1.left.value == 1, "left child with no right child inserted incorrectly"
    assert val1.right is None, "right child non-empty"

    val2 = parent.right.left
    assert val2.left.value == 5, "left child of node in middle of tree is correct"
    assert val2.right.value == 7, "right child of node in middle of tree is correct"

    val3 = parent.right.right.right
    assert val3.left is None, "base level of tree should have no left child"
    assert val3.right is None, "base level of tree should have no right child"

    with pytest.raises(ValueError) as excinfo:
        tree1.insert(1), "Did not raise a value error for trying to insert a duplicate node"
    
    #check if insertion of one node is correct
    tree2 = binary_trees.BST()
    tree2.insert(1)
    val4 = tree2.root
    
    assert val4.left is None
    assert val4.right is None
    assert val4.prev is None


def test_remove():
    """Unit Test for Problem 3: creating a remove method for your BST class"""

    raise NotImplementedError('Unit test for remove method of BST class incomplete')






"""Unit testing file for Linked Lists lab file"""


#import linked_lists.py and pytest
import pytest
import linked_lists



#TA written unit test for problem 2
@pytest.fixture
def setup_linked_lists():
    """
    This function sets up the values used for the following functions:
    test_find()
    test_get()
    
    returns: linked_list, empty linked_list
    """
    list_1 = linked_lists.LinkedList()
    for x in ['a', 'b', 'c', 'd']:
        list_1.append(x)
    list_2 = linked_lists.LinkedList()

    return list_1, list_2

def test_find(setup_linked_lists):
    """Tests find function"""
    list_1, list_2 = setup_linked_lists
    
    #test find element is successful
    node = list_1.find('b')
    assert node.value == 'b', "failed on 2nd list element"

    #test that the correct value error is raised 
    
    #regular list
    with pytest.raises(ValueError) as excinfo:
        list_1.find('q')
    assert excinfo.value.args[0] == "'q' is not in the list"
    #NOTE:This test will fail unless you edit the statement as needed
   

    #empty list
    with pytest.raises(ValueError) as excinfo:
        list_2.find('a')
    assert excinfo.value.args[0] == "'a' is not in the list"
    #NOTE:This test will fail unless you edit the statement as needed


def test_get(setup_linked_lists):
    """Tests get function"""
    list_1, list_2 = setup_linked_lists

    #TEST GET FUNCTION  

    #test get element is successful
    node = list_1.get(2)
    assert node.value == 'c', "failed on 3rd element"

    #test that the correct index error is raised

    #regular list
    with pytest.raises(IndexError) as excinfo:
        list_1.get(9)
    assert excinfo.value.args[0] == "index '9' out of range"
    #NOTE:This test will fail unless you edit the statement as needed

    #negative index
    with pytest.raises(IndexError) as excinfo:
        list_1.get(-2)
    assert excinfo.value.args[0] == "index '-2' out of range"
    #NOTE:This test will fail unless you edit the statement as needed


    #empty list
    with pytest.raises(IndexError) as excinfo:
        list_2.get(0)
    assert excinfo.value.args[0] == "index '0' out of range"
    #NOTE:This test will fail unless you edit the statement as needed


def test_problem3():
    """
    Write unit tests for both the __len__() and __str__() methods.
    """
    raise NotImplementedError("No code written for problem 3 unit test!!")
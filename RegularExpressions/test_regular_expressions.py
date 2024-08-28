"""Unit testing file for Regular Expressions Lab"""


import regular_expressions

def test_prob4():
    """
    Write at least one unit test for problem 4,
    testing to make sure your function correctly finds valid Python identifiers.
    """
    raise NotImplementedError("No code written for problem 4 unit test!!")

def test_prob3():
    # Sets up the pattern
    pattern = regular_expressions.prob3()
    
    # Sets of strings that should work and shouldn't
    good_strings = ["Book store", "Book supplier",
                    "Mattress store", "Mattress supplier",
                    "Grocery store", "Grocery supplier"]
    bad_strings = ["Booky store", "Book Book", "Book Grocery store",
                   "This is a Book store", "Grocery stores rock",
                   "Book storesupplier", " Book store", "Bookstore"]
    
    # Tests all of the good strings
    for s in good_strings:
        assert pattern.search(s), f"'{s}' doesn't match."
        
    # Tests all of the bad strings
    for s in bad_strings:
        assert not pattern.search(s), f"'{s}' matches when it shouldn't."
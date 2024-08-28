"""Unit testing file for the Dynamic Programming lab"""


import dynamic_programming

def test_eat_cake():
    """
    Create a unit test to test your function from problem 6, your eat_cake function.
    You can do this by making sure the matrices produced for the example match up
    with what is in the pdf for the lab.
    """
    raise NotImplementedError("No code written for problem 6 unit test!!")

def test_calc_stopping():
    # Finds the expected value and the stopping index for N = 4.
    expected_val, index = dynamic_programming.calc_stopping(4)

    # Checks to make sure the stopping values are correct.
    assert abs(expected_val - 0.4583) <= 1e-3, "Incorrect expected value"
    assert index == 1, "Incorrect index"

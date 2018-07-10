# dynamic_programming.py
"""Volume 2: Dynamic Programming.
<Name>
<Class>
<Date>
"""

import numpy as np


def calc_stopping(N):
    """Calculate the optimal stopping time and expected value for the
    marriage problem.

    Parameters:
        N (int): The number of candidates.

    Returns:
        (float): The maximum expected value of choosing the best candidate.
        (int): The index of the maximum expected value.
    """
    raise NotImplementedError("Problem 1 Incomplete")


# Problem 2
def graph_stopping_times(N):
    """Graph the optimal percentage of candidates to date optimal
    and expected value for the marriage problem for n=3,4,...,M.

    Parameters:
        M (int): The maximum number of candidates.

    Returns:
        (float): The optimal stopping percent of candidates for N.
    """
    raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
def get_consumption(N, u=np.sqrt):
    """Create the consumption matrix for the given parameters.

    Parameters:
        N (int): Number of pieces given, where each piece of cake is the
            same size.
        u (function): Utility function.

    Returns:
        ((N+1,N+1) ndarray): The consumption matrix.
    """
    raise NotImplementedError("Problem 3 Incomplete")


# Problems 4-6
def eat_cake(T, N, B, u=np.sqrt):
    """Create the value and policy matrices for the given parameters.

    Parameters:
        T (int): Time at which to end (T+1 intervals).
        N (int): Number of pieces given, where each piece of cake is the
            same size.
        B (float): Discount factor, where 0 < B < 1.
        u (function): Utility function.

    Returns:
        A ((N+1,T+1) ndarray): The matrix where the (ij)th entry is the
            value of having w_i cake at time j.
        P ((N+1,T+1) ndarray): The matrix where the (ij)th entry is the
            number of pieces to consume given i pieces at time j.
    """
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 7
def find_policy(T, N, B, u=np.sqrt):
    """Find the most optimal route to take assuming that we start with all of
    the pieces. Show a graph of the optimal policy using graph_policy().

    Parameters:
        T (int): Time at which to end (T+1 intervals).
        N (int): Number of pieces given, where each piece of cake is the
            same size.
        B (float): Discount factor, where 0 < B < 1.
        u (function): Utility function.

    Returns:
        ((N,) ndarray): The matrix describing the optimal percentage to
            consume at each time.
    """
    raise NotImplementedError("Problem 7 Incomplete")

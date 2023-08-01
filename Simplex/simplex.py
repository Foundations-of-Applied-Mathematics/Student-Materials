"""Volume 2: Simplex

<Name>
<Date>
<Class>
"""

import numpy as np


# Problems 1-6
class SimplexSolver(object):
    """Class for solving the standard linear optimization problem

                        minimize        c^Tx
                        subject to      Ax <= b
                                         x >= 0
    via the Simplex algorithm.
    """
    # Problem 1
    def __init__(self, c, A, b):
        """Check for feasibility and initialize the dictionary.

        Parameters:
            c ((n,) ndarray): The coefficients of the objective function.
            A ((m,n) ndarray): The constraint coefficients matrix.
            b ((m,) ndarray): The constraint vector.

        Raises:
            ValueError: if the given system is infeasible at the origin.
        """
        return NotImplementedError("Problem 1 Incomplete")

    # Problem 2
    def _generatedictionary(self, c, A, b):
        """Generate the initial dictionary.

        Parameters:
            c ((n,) ndarray): The coefficients of the objective function.
            A ((m,n) ndarray): The constraint coefficients matrix.
            b ((m,) ndarray): The constraint vector.
        """
        raise NotImplementedError("Problem 2 Incomplete")


    # Problem 3a
    def _pivot_col(self):
        """Return the column index of the next pivot column.
        """
        return NotImplementedError("Problem 3 Incomplete")

    # Problem 3b
    def _pivot_row(self, index):
        """Determine the row index of the next pivot row using the ratio test
        (Bland's Rule).
        """
        return NotImplementedError("Problem 3 Incomplete")

    # Problem 4
    def pivot(self):
        """Select the column and row to pivot on. Reduce the column to a
        negative elementary vector.
        """
        return NotImplementedError("Problem 4 Incomplete")

    # Problem 5
    def solve(self):
        """Solve the linear optimization problem.

        Returns:
            (float) The minimum value of the objective function.
            (dict): The basic variables and their values.
            (dict): The nonbasic variables and their values.
        """
        raise NotImplementedError("Problem 5 Incomplete")

# Problem 6
def prob6(filename='productMix.npz'):
    """Solve the product mix problem for the data in 'productMix.npz'.

    Parameters:
        filename (str): the path to the data file.

    Returns:
        ((n,) ndarray): the number of units that should be produced for each product.
    """
    raise NotImplementedError("Problem 6 Incomplete")

# simplex.py
"""Volume 2: Simplex.
<Name>
<Class>
<Date>

Problems 1-6 give instructions on how to build the SimplexSolver class.
The grader will test your class by solving various linear optimization
problems and will only call the constructor and the solve() methods directly.
Write good docstrings for each of your class methods and comment your code.

prob7() will also be tested directly.
"""

# Problems 1-6
class SimplexSolver(object):
    """Class for solving the standard linear optimization problem

                        maximize        c^Tx
                        subject to      Ax <= b
                                         x >= 0
    via the Simplex algorithm.
    """
    def __init__(self, c, A, b):
        """Check for feasibility and initialize the tableau.

        Parameters:
            c ((n,) ndarray): The coefficients of the objective function.
            A ((m,n) ndarray): The constraint coefficients matrix.
            b ((m,) ndarray): The constraint vector.

        Raises:
            ValueError: if the given system is infeasible at the origin.
        """
        return NotImplementedError("SimplexSolver.__init__() Incomplete")

    def solve(self):
        """Solve the linear optimization problem.

        Returns:
            (float) The maximum value of the objective function.
            (dict): The basic variables and their values.
            (dict): The nonbasic variables and their values.
        """
        raise NotImplementedError("SimplexSolver.solve() Incomplete")


# Problem 7
def prob7(filename='productMix.npz'):
    """Solve the product mix problem for the data in 'productMix.npz'.

    Parameters:
        filename (str): the path to the data file.

    Returns:
        The minimizer of the problem (as an array).
    """
    raise NotImplementedError("Problem 7 Incomplete")

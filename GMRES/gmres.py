# gmres.py
"""Volume 1: GMRES.
<Name>
<Class>
<Date>
"""


# Problems 1 and 2.
def gmres(A, b, x0, k=100, tol=1e-8, plot=False):
    """Calculate approximate solution of Ax=b using the GMRES algorithm.

    Parameters:
        A ((m,m) ndarray): A square matrix.
        b ((m,) ndarray): A 1-D array of length m.
        x0 ((m,) ndarray): The initial guess for the solution to Ax=b.
        k (int): Maximum number of iterations of the GMRES algorithm.
        tol (float): Stopping criterion for size of residual.
        plot (bool): Whether or not to plot convergence (Problem 2).

    Returns:
        ((m,) ndarray): Approximate solution to Ax=b.
        res (float): Residual of the solution.
    """
    raise NotImplementedError("Problem 1 Incomplete")


# Problem 3
def prob3(m=200):
    """For n=-4,-2,0,2,4 create a matrix A= n*I + P where I is the mxm
    identity, and P is an mxm matrix with entries drawn from a normal
    distribution with mean 0 and standard deviation 1/(2*sqrt(m)).
    For each of the given values of n call gmres() with A, a vector of ones called b, an initial guess x0=0, and plot=True

    Parameters:
        m (int): Size of the matrix A.
    """
    raise NotImplementedError("Problem 3 Incomplete")


# Problem 4
def gmres_k(A, b, x0, k=5, tol=1E-8, restarts=50):
    """Implement the GMRES algorithm with restarts. Terminate the algorithm
    when the size of the residual is less than tol or when the maximum number
    of restarts has been reached.

    Parameters:
        A ((m,m) ndarray): A square matrix.
        b ((m,) ndarray): A 1-D array of length m.
        x0 ((m,) ndarray): The initial guess for the solution to Ax=b.
        k (int): Maximum number of iterations of the GMRES algorithm.
        tol (float): Stopping criterion for size of residual.
        restarts (int): Maximum number of restarts. Defaults to 50.

    Returns:
        ((m,) ndarray): Approximate solution to Ax=b.
        res (float): Residual of the solution.
    """
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def time_gmres(m=200):
    """Using the same matrices as in problem 2, plot the time required to
    complete gmres(), gmres_k(), and scipy.sparse.linalg.gmres() with
    restarts. Plot the values of n against the times.

    Parameters:
        m (int): Size of matrix A.
    """
    raise NotImplementedError("Problem 5 Incomplete")

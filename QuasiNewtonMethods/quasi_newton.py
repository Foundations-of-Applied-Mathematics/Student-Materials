# solutions.py
"""Volume 2: Newton and Quasi-Newton Methods.
<Name>
<Class>
<Date>
"""


# Problem 1
def newton(Df, D2f, x0, tol=1e-5, maxiter=20):
    """Use Newton's method to minimize a function f:R^n -> R.

    Parameters:
        Df (function): The first derivative of f. Accepts and returns a NumPy
            array of shape (n,).
        D2f (function): The second dirivative (Hessian) of f. Accepts a NumPy
            array of shape (n,) and returns a NumPy array of shape (n,n).
        x0 ((n,) ndarray): The initial guess.
        tol (float): The stopping tolerance.
        maxiter (int): The maximum number of iterations to compute.

    Returns:
        ((n,) ndarray): The approximate optimizer of f.
        (bool): Whether or not the algorithm converged.
        (int): The number of iterations computed.
    """
    raise NotImplementedError("Problem 1 Incomplete")


# Problem 2
def bfgs(Df, x0, tol=1e-5, maxiter=80):
    """Use BFGS to minimize a function f:R^n -> R.

    Parameters:
        Df (function): The first derivative of f. Accepts and returns a NumPy
            array of shape (n,).
        x0 ((n,) ndarray): The initial guess.
        tol (float): The stopping tolerance.
        maxiter (int): The maximum number of iterations to compute.

    Returns:
        ((n,) ndarray): The approximate optimizer of f.
        (bool): Whether or not the algorithm converged.
        (int): The number of iterations computed.
    """
    raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
def prob3(N=100):
    """Compare newton(), bfgs(), and scipy.optimize.fmin_bfgs() by repeating
    the following N times.
        1. Sample a random initial guess x0 from the 2-D uniform distribution
            over [-3,3]x[-3,3].
        2. Time (separately) newton(), bfgs(), and scipy.optimize.bfgs_fmin()
            for minimizing the Rosenbrock function with an initial guess of x0.
        3. Record the number of iterations from each method.
    Plot the computation times versus the number of iterations with a log-log
    scale, using different colors for each method.
    """
    raise NotImplementedError("Problem 3 Incomplete")


# Problem 4
def gauss_newton(J, r, x0, tol=1e-5, maxiter=10):
    """Solve a nonlinear least squares problem with the Gauss-Newton method.

    Parameters:
        J (function): Jacobian of the residual function. Accepts a NumPy array
            of shape (n,) and returns a NumPy array of shape (m,n).
        r (function): Residual vector function. Accepts a NumPy array of shape
            (n,) and returns an array of shape (m,).
        x0 ((n,) ndarray): The initial guess.
        tol (float): The stopping tolerance.
        maxiter (int): The maximum number of iterations to compute.

    Returns:
        ((n,) ndarray): The approximate optimizer of f.
        (bool): Whether or not the algorithm converged.
        (int): The number of iterations computed.
    """
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def prob5(filename="population.npy"):
    """Load the data from the given file. Fit the data to an exponential model

        phi(x1, x2, x3, t) = x1 exp(x2(t + x3))

    and to a logistic model

        phi(x1, x2, x3, t) = x1 / (1 + exp(-x2(t + x3))).

    Plot the resulting curves along with the data points.
    """
    raise NotImplementedError("Problem 5 Incomplete")

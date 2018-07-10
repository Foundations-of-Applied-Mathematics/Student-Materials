# iPyParallel - Intro to Parallel Programming

def initialize():
    """
    Write a function that initializes a Client object, creates a Direct
    View with all available engines, and imports scipy.sparse as spar on
    all engines.
    """
    raise NotImplementedError("Problem 1 incomplete")

def variables(dx):
    """
    Write a function that accepts a dictionary of variables. Create a Client
    object, a Direct View, and distribute the variables. Then, pull the
    variables in both a blocking and non-blocking format.
    :param dx: Dictionary of variables
    :return: (list of results, list of ASyncResult objects)
    """
    raise NotImplementedError("Problem 2 incomplete")

def prob3(n=1000000):
    """
    Write a function that returns the mean, max, and min for n draws
    from the standard normal distribution where n is default to 1,000,000.
    Use apply_sync() to execute this function across all available engines.
    Print the results as returned by each engine.
    """
    raise NotImplementedError("Problem 3 incomplete")

def prob4():
    """
    Time the function from the previous problem in parallel and serially. Run
    apply_sync() on the function to time in parallel. To time the function
    serially, run the function in a for loop n times, where n is the number
    of engines on your machine. Print the results.
    """
    raise NotImplementedError("Problem 4 incomplete")


def prob5():
    """
    Write a parallel function to find the maximum distance from the given
    New York addresses to its nearest recycle bin. Files for the latitude and
    longitude have been given as "recycle_bins.npy" and "ny_addr.npy".

    Returns:
        address location (ndarray): the furthest address from a recycle bin
        recycle bin location (ndarray): the corresponding recycle bin location
        time (float): the runtime of the function
    """
    raise NotImplementedError("Problem 5 incomplete")

def parallel_trapezoidal_rule(f, a, b, n=200):
    """
    Write a function that accepts a function handle, f, bounds of integration,
    a and b, and a number of points to use, n. Split the interval of
    integration evenly among all available processors and use the trapezoidal
    rule to numerically evaluate the integral over the interval [a,b].

    Parameters:
        f (function handle): the function to evaluate
        a (float): the lower bound of integration
        b (float): the upper bound of integration
        n (int): the number of points to use, defaults to 200
    Returns:
        value (float): the approximate integral calculated by the
            trapezoidal rule
    """
    raise NotImplementedError("Problem 6 incomplete")

def oldprob5(N):
    """
    Accept an integer N that represents the number of draws to take from the
    normal distribution for the distribution X. Take 500,000 draws from this
    distribution and plot a histogram of the results. Split the load evenly
    among all available engines and make the function flexible to the number
    of engines running.
    """
    raise NotImplementedError("Problem 5 incomplete")

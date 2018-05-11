# importance_sampling.py
"""Volume 1: Importance Sampling.
<Name>
<Class>
<Date>
"""

# Problem 1
def prob1(n):
    """Approximate the probability that a random draw from the standard
    normal distribution will be greater than 3.

    Parameters:
    n (int): Number of samples to take

    Returns:
    probability (float): The estimated probability of drawing a 3 from
        the standard normal.
    """
    raise NotImplementedError("Problem 1 Incomplete")

# Problem 2
def IS_integrate(f, g, h, sampler, n):
    """Integrate using Monte-Carlo method with importance sampling
    Parameters:
    f (function): The target distribution.
    g (function): The importance distribution.
    h (function): The indicator function.
    sampler (function): A function that makes random draws from
        the importance distribution.
    n (int): Number of samples to take.

    Returns:
    integral approximation (float): The estimated value of the integral of f
    """
    raise NotImplementedError("Problem 2 Incomplete")

# Problem 3
def prob3():
    """Plot the errors of the regular Monte Carlo integration side by side
    with importance sampling. Use a normal distribution with mu = 4 for
    the importance distribution.
    """
    raise NotImplementedError("Problem 3 Incomplete")

# Problem 4
def prob4():
    """Using alternative 'g_Y' equations, provide four subplots of the error
    between regular Monte Carlo integration compared to importance sampling.
    Keep all of the variances at sigma=1, but let mu vary.
    Plot 1: mu = 4
    Plot 2: mu = -1
    Plot 3: mu = 7
    Plot 4: mu = .25
    """
    raise NotImplementedError("Problem 4 Incomplete")

# Problem 5
def prob5():
    """Using importance sampling, approximate the probability that the tech
    center will have to wait at least 10 minutes to receive 9 calls.
    Return the approximation.
    """
    raise NotImplementedError("Problem 5 Incomplete")

# Problem 6
def prob6():
    """Approximate and return  the probability that a random draw from the
    multivariate standard normal distribution will be less than -1 in
    the x-direction and greater than 1 in the y-direction."""
    raise NotImplementedError("Problem 6 Incomplete")

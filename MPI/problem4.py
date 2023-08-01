# Problem 4
"""The n-dimensional open unit ball is the set U_n = {x in R^n : ||x|| < 1}.
Estimate the volume of U_n by making N draws on each available process except
for the root process. Have the root process print the volume estimate.

Command line arguments:
    n (int): the dimension of the unit ball.
    N (int): the number of random draws to make on each process but the root.

Usage:
    # Estimate the volume of U_2 (the unit circle) with 2000 draws per process.
    $ mpiexec -n 4 python problem4.py 2 2000
    Volume of 2-D unit ball: 3.13266666667      # Results will vary slightly.
"""

# policy_iteration.py
"""Volume 2: Policy Function Iteration.
<Name>
<Class>
<Date>
"""

import numpy as np
import gymnasium as gym
import model_free_RL # For problem 7

# Intialize P for test example
#Left =0
#Down = 1
#Right = 2
#Up= 3

P = {s: {a: [] for a in range(4)} for s in range(4)}
P[0][0] = [(0, 0, 0, False)]
P[0][1] = [(1, 2, -1, False)]
P[0][2] = [(1, 1, 0, False)]
P[0][3] = [(0, 0, 0, False)]
P[1][0] = [(1, 0, -1, False)]
P[1][1] = [(1, 3, 1, True)]
P[1][2] = [(0, 0, 0, False)]
P[1][3] = [(0, 0, 0, False)]
P[2][0] = [(0, 2, -1, False)]
P[2][1] = [(0, 2, -1, False)]
P[2][2] = [(1, 3, 1, True)]
P[2][3] = [(1, 0, 0, False)]
P[3][0] = [(0, 0, 0, True)]
P[3][1] = [(0, 0, 0, True)]
P[3][2] = [(0, 0, 0, True)]
P[3][3] = [(0, 0, 1, True)]


# Problem 1
def value_iteration(P, nS ,nA, beta=1.0, tol=1e-8, maxiter=3000):
    """Perform Value Iteration according to the Bellman optimality principle and iterative policy evaluation.

    Parameters:
        P (dict): The dictionary describing the Markov relationship
                (P[state][action] = [(prob, nextstate, reward, is_terminal)...]).
        nS (int): The number of states.
        nA (int): The number of actions.
        beta (float): The discount rate (between 0 and 1).
        tol (float): The stopping criteria for the value iteration.
        maxiter (int): The maximum number of iterations to run value iteration for

    Returns:
       V (ndarray): The array V approximating the true optimal value function.
       n (int): number of iterations
    """

    raise NotImplementedError("Problem 1 Incomplete")

# Problem 2
def policy_improvement(P, nS, nA, V, beta=1.0):
    """Returns the deterministic policy array for a given array V of the value function according
    to the Policy Improvement theorem.

    Parameters:
        P (dict): The dictionary describing the Markov relationship
                (P[state][action] = [(prob, nextstate, reward, is_terminal)...]).
        nS (int): The number of states.
        nA (int): The number of actions.
        V (ndarray): The array V approximating the true value function.
        beta (float): The discount rate (between 0 and 1).

    Returns:
        policy (ndarray): the deterministic mapping giving an action for a given state
    """
    raise NotImplementedError("Problem 2 Incomplete")

# Problem 3
def iter_policy_eval(P, nS, nA, policy, beta=1.0, tol=1e-8):
    """Computes the value function for a given deterministic policy using iterative policy evaluation.

    Parameters:
        P (dict): The dictionary describing the Markov relationship
                (P[state][action] = [(prob, nextstate, reward, is_terminal)...]).
        nS (int): The number of states.
        nA (int): The number of actions.
        policy (ndarray): The deterministic policy to estimate the value function.
        beta (float): The discount rate (between 0 and 1).
        tol (float): The stopping criteria for the iterative value iteration.

    Returns:
        V (ndarray): The array V approximating the true value function.
    """
    raise NotImplementedError("Problem 3 Incomplete")

# Problem 4
def policy_iteration(P, nS, nA, beta=1.0, tol=1e-8, maxiter=200):
    """Perform Policy Iteration using the principles of policy evaluation and policy improvement.

    Parameters:
        P (dict): The dictionary describing the Markov relationship
                (P[state][action] = [(prob, nextstate, reward, is_terminal)...]).
        nS (int): The number of states.
        nA (int): The number of actions.
        beta (float): The discount rate (between 0 and 1).
        tol (float): The stopping criteria for the value iteration.
        maxiter (int): The maximum number of iterations to run policy iteration for

    Returns:
    	V (ndarray): An array V approximating the true optimal value function.
        policy (ndarray): An array representing the optimal deterministic policy
        n (int): number of iterations that were needed for policy iteration to converge
    """
    raise NotImplementedError("Problem 4 Incomplete")

# Problem 5 and 6
def frozen_lake(basic_case=True, M=1000, render=False):
    """ Finds the optimal deterministic policy to solve the FrozenLake problem using both
    policy and value iteration. It then computes an average of the discounted reward sum
    for M episodes. The function also renders the environment if stated.

    Parameters:
        basic_case (boolean): True for 4x4 and False for 8x8 environments.
        M (int): The number of episodes of FrozenLake-v1 to run.
        render (boolean): Whether to draw the environment.

    Returns (6 items):
        vi_value_func (ndarray): the optimal value function as given by value iteration
        vi_policy (ndarray): The optimal deterministic policy as given by value iteration.
        vi_avg_disct_rewards (float): The mean of the discounted rewards for M episodes of FrozenLake-v1
                                      using the policy from value iteration
        pi_value_func (ndarray): The optimal value function for the optimal policy from policy iteration.
        pi_policy (ndarray): The optimal deterministic policy as given by policy iteration.
        pi_avg_disct_rewards (float): The mean of the discounted rewards for M episodes of FrozenLake-v1
                                      using the policy from policy iteration.
    """
    raise NotImplementedError("Problem 5 Incomplete")

# Problem 6
def run_simulation(env, policy, beta=1.0):
    """ Evaluates a deterministic policy by using it to run a simulation and calculating the total discounted
    reward sum obtained for one episode of the given environment.

    Parameters:
        env (gym environment): The gym environment.
        policy (ndarray): The deterministic policy used to take actions.
        beta (float): The discount factor.

    Returns:
        tot_disct_reward (float): the total discounted reward sum for one episode using the given policy.
    """
    raise NotImplementedError("Problem 6 Incomplete")

# Problem 7
def model_comparison(episodes=1000):
    """ Compare Q-learning to value iteration by creating policies to solve the FrozenLake
    environment using the 8x8 grid and is_slippery=True.

    Parameters:
        episodes (int): the number of episodes to run FrozenLake-v1 for

    Returns (8 values):
        avg_Q_reward (float): the average discounted total reward of Q-learning
        avg_val_iter_reward (float): the average discounted total reward of value iteration
        statement (str): a string of 2-4 sentences that compares the differences between model-based
                         and model-free methods, specifically Q-learning vs. value iteration
    """
    raise NotImplementedError("Problem 7 Incomplete")
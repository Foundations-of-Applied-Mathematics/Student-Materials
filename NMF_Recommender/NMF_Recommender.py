import numpy as np
import pandas as pd
from sklearn.decomposition import NMF

class NMFRecommender:

    def __init__(self, random_state=15, rank=2, maxiter=200, tol=1e-3):
        """
        Save the parameter values as attributes.
        """
        raise NotImplementedError("Problem incomplete")
  

    def _initialize_matrices(self, m, n):
        """
        Initialize the W and H matrices.
        
        Parameters:
            m (int): the number of rows
            n (int): the number of columns
        Returns:
            W ((m,k) array)
            H ((k,n) array)
        """
        raise NotImplementedError("Problem incomplete")


    def _compute_loss(self, V, W, H):
        """
        Compute the loss of the algorithm according to the 
        Frobenius norm.
        
        Parameters:
            V ((m,n) array): the array to decompose
            W ((m,k) array)
            H ((k,n) array)
        Returns:
            Frobenius norm of V - WH (float)
        """
        raise NotImplementedError("Problem incomplete")


    def _update_matrices(self, V, W, H):
        """
        The multiplicative update step to update W and H
        Return the new W and H (in that order).
        
        Parameters:
            V ((m,n) array): the array to decompose
            W ((m,k) array)
            H ((k,n) array)
        Returns:
            New W ((m,k) array)
            New H ((k,n) array)
        """
        raise NotImplementedError("Problem incomplete")


    def fit(self, V):
        """
        Fits W and H weight matrices according to the multiplicative 
        update algorithm. Save W and H as attributes and return them.
        
        Parameters:
            V ((m,n) array): the array to decompose
        Returns:
            W ((m,k) array)
            H ((k,n) array)
        """
        raise NotImplementedError("Problem incomplete")


    def reconstruct(self):
        """
        Reconstruct and return the decomposed V matrix for comparison against 
        the original V matrix. Use the W and H saved as attrubutes.
        
        Returns:
            V ((m,n) array): the reconstruced version of the original data
        """
        raise NotImplementedError("Problem incomplete")


def prob4(rank=2):
    """
    Run NMF recommender on the grocery store example.
    
    Returns:
        W ((m,k) array)
        H ((k,n) array)
        The number of people with higher component 2 than component 1 scores (float)
    """
    V = np.array([[0, 1, 0, 1, 2, 2],
                  [2, 3, 1, 1, 2, 2],
                  [1, 1, 1, 0, 1, 1],
                  [0, 2, 3, 4, 1, 1],
                  [0, 0, 0, 0, 1, 0]])
                  
    raise NotImplementedError("Problem incomplete")


def prob5(filename='artist_user.csv'):
    """
    Read in the file `artist_user.csv` as a Pandas dataframe. Find the optimal
    value to use as the rank as described in the lab pdf. Return the rank and the reconstructed matrix V.
    
    Returns:
        rank (int): the optimal rank
        V ((m,n) array): the reconstructed version of the data
    """
    raise NotImplementedError("Problem incomplete")


def discover_weekly(userid, V):
    """
    Create the recommended weekly 30 list for a given user.
    
    Parameters:
        userid (int): which user to do the process for
        V ((m,n) array): the reconstructed array
        
    Returns:
        recom (list[str]): a list of strings that contains the names of the recommended artists
    """
    raise NotImplementedError("Problem incomplete")
    
    
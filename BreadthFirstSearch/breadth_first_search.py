# breadth_first_search.py
"""Volume 2: Breadth-First Search.
<Name>
<Class>
<Date>
"""


# Problems 1-3: Implement the following class
class Graph(object):
    """A graph object, stored as an adjacency dictionary. Each node in the
    graph is a key in the dictionary. The value of each key is a list of the
    corresponding node's neighbors.

    Attributes:
        dictionary: the adjacency list of the graph.
    """

    def __init__(self, adjacency):
        """Store the adjacency dictionary as a class attribute."""
        self.dictionary = adjacency

    # Problem 1
    def __str__(self):
        """String representation: a view of the adjacency dictionary.

        Example:
            >>> test = {'A':['B'], 'B':['A', 'C',], 'C':['B']}
            >>> print(Graph(test))
            A: B
            B: A; C
            C: B
        """
        raise NotImplementedError("Problem 1 Incomplete")

    # Problem 2
    def traverse(self, start):
        """Begin at 'start' and perform a breadth-first search until all
        nodes in the graph have been visited. Return a list of values,
        in the order that they were visited.

        Parameters:
            start: the node to start the search at.

        Returns:
            the list of visited nodes (in order of visitation).

        Raises:
            ValueError: if 'start' is not in the adjacency dictionary.

        Example:
            >>> test = {'A':['B'], 'B':['A', 'C',], 'C':['B']}
            >>> Graph(test).traverse('B')
            ['B', 'A', 'C']
        """
        raise NotImplementedError("Problem 2 Incomplete")

    # Problem 3
    def shortest_path(self, start, target):
        """Begin at the node containing 'start' and perform a breadth-first
        search until the node containing 'target' is found. Return a list
        containg the shortest path from 'start' to 'target'. If either of
        the inputs are not in the adjacency graph, raise a ValueError.

        Parameters:
            start: the node to start the search at.
            target: the node to search for.

        Returns:
            A list of nodes along the shortest path from start to target,
                including the endpoints.

        Example:
            >>> test = {'A':['B', 'F'], 'B':['A', 'C'], 'C':['B', 'D'],
            ...         'D':['C', 'E'], 'E':['D', 'F'], 'F':['A', 'E', 'G'],
            ...         'G':['A', 'F']}
            >>> Graph(test).shortest_path('A', 'G')
            ['A', 'F', 'G']
        """
        raise NotImplementedError("Problem 3 Incomplete")


# Problem 4: Write the following function
def convert_to_networkx(dictionary):
    """Convert 'dictionary' to a networkX object and return it."""
    raise NotImplementedError("Problem 4 Incomplete")


# Problems 5-7: Implement the following class
class BaconSolver(object):
    """Class for solving the Kevin Bacon problem."""

    # Problem 5
    def __init__(self, filename="movieData.txt"):
        """Initialize the networkX graph with data from the specified
        file. Store the graph as a class attribute. Also store the collection
        of actors in the file as an attribute.
        """
        raise NotImplementedError("Problem 5 Incomplete")

    # Problem 6
    def path_to_bacon(self, start, target="Bacon, Kevin"):
        """Find the shortest path from 'start' to 'target'."""
        raise NotImplementedError("Problem 6 Incomplete")

    # Problem 7
    def bacon_number(self, start, target="Bacon, Kevin"):
        """Return the Bacon number of 'start'."""
        raise NotImplementedError("Problem 7 Incomplete")

    # Problem 7
    def average_bacon(self, target="Bacon, Kevin"):
        """Calculate the average Bacon number in the data set.
        Note that actors are not guaranteed to be connected to the target.

        Parameters:
            target (str): the node to search the graph for.

        Returns:
            (float): the average (finite) Bacon number
            (int): the number of actors not connected to the target.
        """
        raise NotImplementedError("Problem 7 Incomplete")

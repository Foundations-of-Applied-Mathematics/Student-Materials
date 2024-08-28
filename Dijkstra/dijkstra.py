# dijkstra.py
"""Volume 2: Dijkstra's Algorithm
<Name>
<Class>
<Date>
"""

# imports
from math import sqrt
from queue import PriorityQueue
from collections import defaultdict

class Edge:
    """An edge object, which wraps the node and weight attributes into one
    object, allowing for insertion/deletion from a set using just
    the node attribute

    Attributes:
        node (str): the value for the node the edge is pointing to
        weight (int): the weight of the edge
    """
    def __init__(self, node, weight):
        self.node = node
        self.weight = weight

    def __hash__(self):
        """Use only node attribute for hashing"""
        return hash(self.node)

    def __eq__(self, other):
        """Use only node attribute for equality"""
        if isinstance(other, Edge):
            return self.node == other.node
        return self.node == other

    def __str__(self):
        """String representation: a tuple-like view of the node and weight"""
        return f"({str(self.node)}, {str(self.weight)})"

    def __repr__(self):
        """Repr is used when edges are displayed in a set"""
        return f"Edge({repr(self.node)}, {repr(self.weight)})"

# Problems 1-3
class Graph:
    """A graph object, stored as an adjacency dictionary. Each node in the
    graph is a key in the dictionary. The value of each key is a set of
    the corresponding node's neighbors (stored as tuples).

    Attributes:
        d (dict): the adjacency dictionary of the graph.
        directed (bool): true if the graph is a directed graph.
    """
    # Problem 1
    def __init__(self, adjacency={}, directed=False):
        """Store the adjacency dictionary and directed as class attributes"""
        raise NotImplementedError("Problem 1 Incomplete")

    def __str__(self):
        """String representation: a view of the adjacency dictionary."""
        return str(self.d)

    # Problem 1
    def add_node(self, n):
        """Add n to the graph (with no initial edges) if it is not already
        present.

        Parameters:
            n: the label for the new node.
        """
        raise NotImplementedError("Problem 1 Incomplete")

    # Problem 1
    def add_edge(self, u, v, weight=1.0):
        """Add a weighted edge between node u and node v.
        If an edge already exists between u and v, simply update the weight.
        Also add u and v to the graph if they are not already present.

        Parameters:
            u: a node label.
            v: a node label.
        """
        raise NotImplementedError("Problem 1 Incomplete")

    # Problem 1
    def remove_node(self, n):
        """Remove n from the graph, including all edges adjacent to it.

        Parameters:
            n: the label for the node to remove.

        Raises:
            KeyError: if n is not in the graph.
        """
        raise NotImplementedError("Problem 1 Incomplete")

    # Problem 1
    def remove_edge(self, u, v):
        """Remove the edge starting at u and ending at v.

        Parameters:
            u: a node label.
            v: a node label.

        Raises:
            KeyError: if u or v are not in the graph, or if there is no
                edge from u to v.
        """
        raise NotImplementedError("Problem 1 Incomplete")

    # Problem 2
    def shortest_path(self, source, target):
        """Begin Dijkstra's at the source node and proceed until the target is
        found. Return an integer denoting the sum of weights along the shortest
        path from source to target along with a list of the path itself,
        including endpoints.

        Parameters:
            source: the node to start the search at.
            target: the node to search for.

        Returns:
            An int denoting the sum of weights along the shortest path
                from source to target
            A list of nodes along the shortest path from source to target,
                including the endpoints. The path should contain strings
                representing the nodes, not edge objects

        Raises:
            KeyError: if the source or target nodes are not in the graph.
        """
        raise NotImplementedError("Problem 2 Incomplete")


# Constants
FILE_PATH = r"bathymetry.tt3"
START_LONG_LAT = (131.75, -5.52)
END_LONG_LAT = (128.657, -3.576)
METERS_PER_DEG = 111111 # Approximation for meters per degree of lat/long
FAULT_PLANE_RADIUS = 103587.2508/2 # Approximate radius for the fault plane, in meters
FAULT_RADIUS_DEG = FAULT_PLANE_RADIUS / METERS_PER_DEG  # radius of the fault plane approximated to degrees

class TsunamiModel(Graph):
    """A class representing a model for calculating time-based tsunami paths
    between two locations given the bathymetric (sea-depth) data of the area.

    Attributes:
        fault_plane_radius (float): Describes the radius (in arc-degrees)
        of the fault plane over which the tsunami forms, which is used to
        determine the proper starting point in time prediction.
        ncols, nrows (int): The number of columns and rows, respectively,
        in the bathymetry grid,
        lat_llcorner, long_llcorner (float) The longitude and latitude coordinates,
        respectively, of the lower-left corner of the bathymetry data grid.
        cellsize (float): The distance (in arc-degrees) between any two grid
        points in the bathymetric data.
        depths_grid (list[list[float]]): The grid of bathymetric data, each value
        represents the sea-depth at that location.
        long_lat_grid (list[list[float]]): The grid of latitude/longitude
        cooridnates corresponding to the locations of each bathymetric
        measurement in grid.
        start_point (tuple): Indeces corresponding to the starting point in grid
        of the tsunami.
        end_point (tuple): Indeces corresponding to the destination point in grid
        of the tsunami.

    Methods:
        calculate_tsunami_path(): Returns the estimated time (in minutes)
        and path for a tsunami to travel between start_point
        and end_point.
    """

    # Problems 3-4
    def __init__(self, filename, start_long_lat, end_long_lat,
                 fault_plane_radius=FAULT_RADIUS_DEG):
        """
        Initializes the TimeModel.

        Parameters:
        - start_long_lat (tuple): Tuple containing start longitude and latitude
        which represents the tsunami's origin point.
        - end_long_lat (tuple): Tuple containing end longitude and latitude
        which represents the location in the tsunami's path.
        - fault_plane_radius (float): Describes the radius (in arc-degrees)
        of the fault plane over which the tsunami forms, which is used to
        determine the proper starting point in time prediction.
        """
        # Call Graph constructor

        # Read in bathymetry data from file

        # Process longitude and latitude data
        self.fault_plane_radius = None

        raise NotImplementedError("Problem 3 Incomplete")

    # Problem 3
    def _read_file(self, filename):
        """
        Reads in the contents of the bathymetry datafile with filename
        and creates instance attributes with the relevant data.
        """

        self.ncols = None
        self.nrows = None
        self.long_llcorner = None
        self.lat_llcorner = None
        self.cellsize = None

        self.depths_grid = None
        raise NotImplementedError("Problem 3 Incomplete")

    # Problem 3
    def _generate_long_lat_grid(self):
        """
        Generates a grid of longitude and latitude coordinates.

        Returns:
        - (list[list[float]]): Grid of longitude and latitude coordinates.
        """
        raise NotImplementedError("Problem 3 Incomplete")

    # Problem 4
    def _shifted_start(self, start_point, end_point):
        """
        Computes the shifted start value to line up with the edge of the fault
        plane in the direction of end_point.
        """
        raise NotImplementedError("Problem 4 Incomplete")

    # Problem 4
    def _long_and_lat(self, start_long_lat, end_long_lat):
        """
        Generates the instance attributes associated with latitude and
        longitude coordinates. Specifically, the starting and ending
        grid indices and the grid of longitude and latitude coordinates
        """
        self.long_lat_grid = None

        self.start_point = None
        self.end_point = None
        raise NotImplementedError("Problem 4 Incomplete")

    def _get_nearest_point(self, long_lat_point):
        """
        Finds the closest grid point to a given longitude and latitude point.

        Parameters:
        - long_lat_point (tuple): Latitude and longitude coordinates.

        Returns:
        - (tuple): Indices of the closest grid point.
        """
        closest_value_diff = float("inf")  # Initialize a variable to track the closest value difference
        closest_position = (0, 0) # Initialize a variable to store the closest position

        # Iterate through the grid to find the closest grid point
        for i in range(len(self.long_lat_grid)):
            for j in range(len(self.long_lat_grid[i])):
                current_tuple = self.long_lat_grid[i][j]  # Get current grid point coordinates

                # Calculate the absolute difference between the points
                value_diff = sum(abs(x - y) for x, y in zip(long_lat_point, current_tuple))

                # Check if the current grid point is closer than the previously closest one
                # and self.depths_grid[closest_position[0]][closest_position[1]] < 0
                thing = self.depths_grid[i][j]
                if value_diff < closest_value_diff and thing < 0:
                    closest_value_diff = value_diff  # Update the closest value difference
                    closest_position = (i, j)  # Update the closest position
        return closest_position   # Return the indices of the closest grid point

    # Problem 5
    def _get_neighbors(self, node):
        """
        Retrieves neighboring nodes of a given node within the grid boundaries.
        A neighboring node is valid if it is in bounds and has a
        negative elevation.

        Parameters:
        - node (tuple): Coordinates of the current node (row, col).

        Returns:
        - (list): List of neighboring nodes.
        """
        raise NotImplementedError("Problem 5 Incomplete")

    # Problem 5
    def _convert_path_to_long_lat(self, path):
        """
        Converts a path of grid points to a list of longitude and latitude coordinates.

        Parameters:
        - path (list): List of grid points.

        Returns:
        - (list): List of longitude and latitude coordinates.
        """
        raise NotImplementedError("Problem 5 Incomplete")

    # Problem 5
    def get_time(self, d1, d2):
        """
        Estimates the time (in seconds) for a tsunami to travel between two
        adjacent grid points with depths d1 and d2 respectively.
        """
        raise NotImplementedError("Problem 5 Incomplete")

    # Problem 6
    def _generate_graph(self):
        """
        Generates the graph used for Tsunami time prediction.
        Specifically, uses method of the Graph class to add edges
        between grid points below sea level, weighted by the get_time() method.
        Nodes are labeled by their zero-indexed location in grid.
        """
        raise NotImplementedError("Problem 6 Incomplete")

    # Problem 6
    def calculate_tsunami_path(self):
        """
        Implementation of Dijkstra's algorithm on a grid to find the shortest
        time for a tsunami to get from self.start_point to self.end_point

        Returns:
        - (float): Total time taken in minutes for the shortest path.
        - (list): Shortest path in longitude and latitude coordinates.
        """

        raise NotImplementedError("Problem 6 Incomplete")








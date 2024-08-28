"""Unit testing file for Linked Lists lab file"""

import pytest
from dijkstra import Edge, Graph


# Problem 1
def test_graph():
    """Test code for the graph class creation methods"""
    raise NotImplementedError("Test not Written!")

def test_shortest_path():
    """Test code for the shortest_path() method of the Graph class"""
    # Undirected graph
    graph = Graph({'A': {Edge('B', 1), Edge('D', 100)},
                   'B': {Edge('A', 1), Edge('C', 1), Edge('D', 100)},
                   'C': {Edge('B', 1), Edge('D', 1)},
                   'D': {Edge('A', 100), Edge('B', 100), Edge('C', 1)}})

    v1, t1 = graph.shortest_path('A', 'D')
    assert v1 == 3, "Incorrect weight sum"
    assert t1 == ['A', 'B', 'C', 'D'], "Incorrect path"

    graph.remove_edge('A', 'B')
    v2, t2 = graph.shortest_path('A', 'D')
    assert v2 == 100, "Incorrect weight sum"
    assert t2 == ['A', 'D'], "Incorrect path"

    with pytest.raises(KeyError):
        graph.shortest_path('A', 'Not a node')

    # Directed graph
    graph = Graph({'A': {Edge('D', 100)},
                   'B': {Edge('A', 1), Edge('D', 100)},
                   'C': {Edge('B', 1), Edge('D', 1)},
                   'D': {Edge('A', 100), Edge('B', 100), Edge('C', 1)}},
                  directed=True)

    v1, t1 = graph.shortest_path('A', 'D')
    assert v1 == 100, "Incorrect weight sum"
    assert t1 == ['A', 'D'], "Incorrect path"

    graph.add_edge('A', 'D', weight=1)
    v2, t2 = graph.shortest_path('A', 'B')
    assert v2 == 3, "Incorrect weight sum"
    assert t2 == ['A', 'D', 'C', 'B'], "Incorrect path"


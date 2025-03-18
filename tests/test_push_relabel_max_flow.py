import pytest
from src.push_relabel_max_flow import PushRelabelMaxFlow

def test_simple_max_flow():
    """
    Test a simple max flow scenario
    """
    # Create graph with 4 vertices
    network = PushRelabelMaxFlow(4)
    
    # Add edges
    network.add_edge(0, 1, 10)
    network.add_edge(0, 2, 8)
    network.add_edge(1, 2, 2)
    network.add_edge(1, 3, 5)
    network.add_edge(2, 3, 7)
    
    # Compute max flow from source (0) to sink (3)
    max_flow = network.max_flow(0, 3)
    
    # Expected max flow is 13 (10 through path 0->1->3 and 3 through path 0->2->3)
    assert max_flow == 13

def test_fully_connected_graph():
    """
    Test max flow in a fully connected graph
    """
    network = PushRelabelMaxFlow(3)
    
    # Add edges between all vertices
    network.add_edge(0, 1, 10)
    network.add_edge(0, 2, 8)
    network.add_edge(1, 2, 5)
    network.add_edge(1, 0, 2)
    network.add_edge(2, 0, 3)
    network.add_edge(2, 1, 4)
    
    max_flow = network.max_flow(0, 2)
    
    # Exact flow depends on algorithm implementation
    assert max_flow == 10

def test_invalid_vertices():
    """
    Test error handling for invalid vertices
    """
    network = PushRelabelMaxFlow(3)
    
    # Test invalid source/sink
    with pytest.raises(ValueError):
        network.max_flow(-1, 2)
    
    with pytest.raises(ValueError):
        network.max_flow(3, 2)
    
    with pytest.raises(ValueError):
        network.max_flow(1, 1)

def test_no_path():
    """
    Test scenario with no path between source and sink
    """
    network = PushRelabelMaxFlow(4)
    
    # No edges connecting source and sink
    network.add_edge(0, 1, 10)
    network.add_edge(2, 3, 5)
    
    max_flow = network.max_flow(0, 3)
    
    assert max_flow == 0

def test_multiple_paths():
    """
    Test max flow with multiple possible paths
    """
    network = PushRelabelMaxFlow(5)
    
    # Complex graph with multiple paths
    network.add_edge(0, 1, 10)
    network.add_edge(0, 2, 8)
    network.add_edge(1, 3, 5)
    network.add_edge(2, 3, 7)
    network.add_edge(1, 4, 15)
    network.add_edge(3, 4, 10)
    
    max_flow = network.max_flow(0, 4)
    
    # Expected max flow is 22
    assert max_flow == 22
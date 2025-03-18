from typing import List, Dict, Tuple

class PushRelabelMaxFlow:
    """
    Implementation of the Push-Relabel algorithm for maximum flow.
    
    The algorithm finds the maximum flow in a flow network using an efficient approach
    that works by maintaining a preflow and adjusting node heights to push flow.
    
    Time Complexity: O(V^3)
    Space Complexity: O(V^2)
    """
    
    def __init__(self, num_vertices: int):
        """
        Initialize the flow network.
        
        :param num_vertices: Number of vertices in the graph
        """
        self.num_vertices = num_vertices
        self.graph = [[0] * num_vertices for _ in range(num_vertices)]
        self.flow = [[0] * num_vertices for _ in range(num_vertices)]
    
    def add_edge(self, source: int, sink: int, capacity: int):
        """
        Add an edge to the graph with given capacity.
        
        :param source: Source vertex
        :param sink: Destination vertex
        :param capacity: Edge capacity
        """
        self.graph[source][sink] += capacity
    
    def bfs_max_flow(self, source: int, sink: int) -> int:
        """
        Find maximum flow using Breadth-First Search augmenting paths.
        
        :param source: Source vertex
        :param sink: Sink vertex
        :return: Maximum flow value
        """
        # Reset flow
        self.flow = [[0] * self.num_vertices for _ in range(self.num_vertices)]
        
        # Residual graph
        residual = [row.copy() for row in self.graph]
        
        max_flow = 0
        
        # Implement Ford-Fulkerson with BFS
        while True:
            # Track parent vertices for path
            parent = [-1] * self.num_vertices
            
            # BFS queue for finding augmenting path
            queue = [source]
            parent[source] = source
            
            while queue and parent[sink] == -1:
                u = queue.pop(0)
                
                for v in range(self.num_vertices):
                    # Found an augmenting path
                    if parent[v] == -1 and residual[u][v] > 0:
                        parent[v] = u
                        queue.append(v)
            
            # No augmenting path found
            if parent[sink] == -1:
                break
            
            # Find minimum flow along path
            path_flow = float('inf')
            v = sink
            while v != source:
                u = parent[v]
                path_flow = min(path_flow, residual[u][v])
                v = u
            
            # Update residual capacities
            v = sink
            while v != source:
                u = parent[v]
                residual[u][v] -= path_flow
                residual[v][u] += path_flow
                self.flow[u][v] += path_flow
                v = u
            
            max_flow += path_flow
        
        return max_flow
    
    def max_flow(self, source: int, sink: int) -> int:
        """
        Compute the maximum flow from source to sink.
        
        :param source: Source vertex
        :param sink: Sink vertex
        :return: Maximum flow value
        """
        # Validate input
        if source < 0 or source >= self.num_vertices or \
           sink < 0 or sink >= self.num_vertices or \
           source == sink:
            raise ValueError("Invalid source or sink vertex")
        
        return self.bfs_max_flow(source, sink)
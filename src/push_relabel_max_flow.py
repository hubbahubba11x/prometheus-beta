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
        self.height = [0] * num_vertices
        self.excess_flow = [0] * num_vertices
    
    def add_edge(self, source: int, sink: int, capacity: int):
        """
        Add an edge to the graph with given capacity.
        
        :param source: Source vertex
        :param sink: Destination vertex
        :param capacity: Edge capacity
        """
        self.graph[source][sink] += capacity
    
    def initialize_preflow(self, source: int):
        """
        Initialize the preflow from the source vertex.
        
        :param source: Source vertex
        """
        # Reset height, excess flow
        self.height = [0] * self.num_vertices
        self.excess_flow = [0] * self.num_vertices
        self.flow = [[0] * self.num_vertices for _ in range(self.num_vertices)]
        
        # Set source height to number of vertices
        self.height[source] = self.num_vertices
        
        # Push initial flow from source to its neighbors
        for v in range(self.num_vertices):
            if self.graph[source][v] > 0:
                self.flow[source][v] = self.graph[source][v]
                self.flow[v][source] = -self.graph[source][v]
                self.excess_flow[v] = self.graph[source][v]
                self.excess_flow[source] -= self.graph[source][v]
    
    def push(self, u: int, v: int):
        """
        Push excess flow from vertex u to vertex v.
        
        :param u: Source vertex
        :param v: Destination vertex
        """
        # Compute the amount of flow to push
        delta = min(
            self.excess_flow[u], 
            self.graph[u][v] - self.flow[u][v]
        )
        
        # Update flows
        self.flow[u][v] += delta
        self.flow[v][u] -= delta
        
        # Update excess flows
        self.excess_flow[u] -= delta
        self.excess_flow[v] += delta
    
    def relabel(self, u: int):
        """
        Relabel the height of vertex u.
        
        :param u: Vertex to relabel
        """
        # Find minimum height of admissible neighbors
        min_height = float('inf')
        for v in range(self.num_vertices):
            if self.graph[u][v] > self.flow[u][v]:
                min_height = min(min_height, self.height[v])
        
        # Increase height of u
        self.height[u] = min_height + 1
    
    def max_flow(self, source: int, sink: int) -> int:
        """
        Compute the maximum flow from source to sink using Push-Relabel algorithm.
        
        :param source: Source vertex
        :param sink: Sink vertex
        :return: Maximum flow value
        """
        # Validate input
        if source < 0 or source >= self.num_vertices or \
           sink < 0 or sink >= self.num_vertices or \
           source == sink:
            raise ValueError("Invalid source or sink vertex")
        
        # Initialize preflow
        self.initialize_preflow(source)
        
        # Overflowing vertices list
        overflowing = [v for v in range(self.num_vertices) if v != source and v != sink]
        
        while overflowing:
            u = overflowing.pop(0)
            
            # Initial height is current vertex height
            initial_height = self.height[u]
            
            # Push excess flow to admissible neighbors
            for v in range(self.num_vertices):
                # Push if capacity allows and u's height > v's height 
                if (self.graph[u][v] > self.flow[u][v]) and (self.height[u] > self.height[v]):
                    # Compute maximum flow to push
                    push_amount = min(
                        self.excess_flow[u], 
                        self.graph[u][v] - self.flow[u][v]
                    )
                    
                    # Push the flow
                    self.flow[u][v] += push_amount
                    self.flow[v][u] -= push_amount
                    
                    # Update excess flows
                    self.excess_flow[u] -= push_amount
                    self.excess_flow[v] += push_amount
                    
                    # If vertex v would have excess and was not already overflowing, add it
                    if v != source and v != sink and push_amount > 0 and self.excess_flow[v] > 0:
                        overflowing.append(v)
            
            # If still has excess after pushing, relabel
            if self.excess_flow[u] > 0:
                # If height didn't increase, vertex is stuck
                self.relabel(u)
                if self.height[u] > initial_height:
                    overflowing.append(u)
        
        # Return the total flow out of the source/into the sink
        return max(0, sum(self.flow[source]))
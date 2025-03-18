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
    
    def discharge(self, u: int):
        """
        Discharge excess flow from vertex u.
        
        :param u: Vertex to discharge
        """
        while self.excess_flow[u] > 0:
            # Try all neighbors
            flow_pushed = False
            for v in range(self.num_vertices):
                # Push if there's residual capacity and u is higher than v
                if (self.graph[u][v] > self.flow[u][v]) and (self.height[u] > self.height[v]):
                    self.push(u, v)
                    flow_pushed = True
                    break
            
            # If no push possible, relabel
            if not flow_pushed:
                self.relabel(u)
    
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
        
        # Work queue of overflowing vertices, excluding source and sink
        work_list = [v for v in range(self.num_vertices) if v != source and v != sink]
        
        while work_list:
            u = work_list.pop(0)
            
            # Store old excess to detect change
            old_excess = self.excess_flow[u]
            
            # Discharge vertex
            self.discharge(u)
            
            # If excess changed, reconsider vertex
            if self.excess_flow[u] > 0 and old_excess == 0:
                work_list.append(u)
        
        # Return the total flow to the sink
        return max(0, sum(self.flow[source]))  # Maximum flow into sink
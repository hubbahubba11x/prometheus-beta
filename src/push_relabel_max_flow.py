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
    
    def add_edge(self, source: int, sink: int, capacity: int):
        """
        Add an edge to the graph with given capacity.
        
        :param source: Source vertex
        :param sink: Destination vertex
        :param capacity: Edge capacity
        """
        self.graph[source][sink] += capacity
    
    def dinic_max_flow(self, source: int, sink: int) -> int:
        """
        Find maximum flow using Dinic's algorithm.
        
        :param source: Source vertex
        :param sink: Sink vertex
        :return: Maximum flow value
        """
        # Tracks residual graph 
        residual = [row.copy() for row in self.graph]
        
        # Total flow
        max_flow = 0
        
        # Level tracking for BFS 
        def bfs_level_graph() -> bool:
            level[:] = [-1] * self.num_vertices
            level[source] = 0
            queue = [source]
            
            while queue:
                u = queue.pop(0)
                
                for v in range(self.num_vertices):
                    # Find admissible edges with remaining capacity 
                    if level[v] == -1 and residual[u][v] > 0:
                        level[v] = level[u] + 1
                        queue.append(v)
            
            return level[sink] != -1
        
        # DFS to find augmenting path 
        def dfs_blocking_flow(u: int, flow: int) -> int:
            # Sink reached
            if u == sink:
                return flow
            
            for v in range(self.num_vertices):
                # Find admissible edge with remaining capacity 
                if (level[v] == level[u] + 1) and (residual[u][v] > 0):
                    curr_flow = dfs_blocking_flow(
                        v, 
                        min(flow, residual[u][v])
                    )
                    
                    # Push flow 
                    if curr_flow > 0:
                        residual[u][v] -= curr_flow
                        residual[v][u] += curr_flow
                        return curr_flow
            
            return 0
        
        # Level array to track BFS 
        level = [-1] * self.num_vertices
        
        # Dinic's algorithm main loop 
        while bfs_level_graph():
            # While augmenting path exists
            while True:
                flow = dfs_blocking_flow(source, float('inf'))
                if flow == 0:
                    break
                max_flow += flow
        
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
        
        return self.dinic_max_flow(source, sink)
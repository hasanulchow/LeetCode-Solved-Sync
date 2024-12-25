from collections import defaultdict, deque
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        Calculates the results of a list of queries, each asking for the result of a division of two variables.
        The equations and their values are used to form a graph of divisions.

        Args:
        equations (List[List[str]]): List of equations, where each equation is a pair of variables.
        values (List[float]): List of values representing the result of each equation.
        queries (List[List[str]]): List of queries asking for division results between two variables.

        Returns:
        List[float]: Results of each query, either a calculated value or -1 if no path exists.
        """
        # Build an adjacency list representing the graph of equations and their relationships
        adjacencyList = defaultdict(list)

        # Populate the adjacency list based on the given equations and their respective values
        for i, eq in enumerate(equations):
            a, b = eq
            adjacencyList[a].append([b, values[i]])        # a -> b with value
            adjacencyList[b].append([a, 1 / values[i]])    # b -> a with reciprocal value

        # Function to perform a BFS to find the division result from src to trg
        def bfs(src, trg):
            # If either source or target is not in the graph, return -1
            if src not in adjacencyList or trg not in adjacencyList:
                return -1

            # Queue for BFS (stores current node and accumulated product)
            q = deque()
            visited = set()  # Set to track visited nodes to prevent cycles

            # Start BFS from the source with an initial product of 1
            q.append([src, 1])
            visited.add(src)

            # Perform BFS until the queue is empty or target is found
            while q:
                n, w = q.popleft()

                # If we have reached the target, return the accumulated weight
                if n == trg:
                    return w

                # Traverse the neighbors of the current node
                for neighbor, weight in adjacencyList[n]:
                    if neighbor not in visited:
                        q.append([neighbor, w * weight])  # Multiply by the edge weight
                        visited.add(neighbor)  # Mark the neighbor as visited

            # If no path is found, return -1
            return -1

        # Process all queries and return the results using BFS for each
        return [bfs(query[0], query[1]) for query in queries]

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # If the graph is empty, return None
        if not node:
            return node
        
        # Initialize a queue for BFS traversal and a dictionary to store cloned nodes
        q = deque([node])  # Start BFS with the given node
        clones = {node.val: Node(node.val, [])}  # Clone the starting node and store it
        
        # Perform BFS traversal
        while q:
            # Get the current node from the queue
            cur = q.popleft()
            # Get the clone of the current node
            cur_clone = clones[cur.val]
            
            # Iterate through all the neighbors of the current node
            for ngbr in cur.neighbors:
                # If the neighbor hasn't been cloned yet
                if ngbr.val not in clones:
                    # Clone the neighbor and add it to the dictionary
                    clones[ngbr.val] = Node(ngbr.val, [])
                    # Add the neighbor to the queue for further exploration
                    q.append(ngbr)
                
                # Add the cloned neighbor to the neighbors list of the current clone
                cur_clone.neighbors.append(clones[ngbr.val])
        
        # Return the clone of the starting node
        return clones[node.val]

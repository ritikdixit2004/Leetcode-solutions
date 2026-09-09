

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        # Dictionary to save the visited nodes and their respective clones
        cloned = {}
        
        def dfs(curr_node):
            # If the node was already cloned, return the clone from the dictionary
            if curr_node in cloned:
                return cloned[curr_node]
            
            # Create a clone for the current node
            clone = Node(curr_node.val)
            # Add the clone to the dictionary before traversing neighbors to avoid cycles
            cloned[curr_node] = clone
            
            # Iterate through the neighbors to clone them as well
            for neighbor in curr_node.neighbors:
                clone.neighbors.append(dfs(neighbor))
                
            return clone
            
        return dfs(node)
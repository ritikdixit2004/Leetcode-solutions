"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        # 'curr' tracks our position on the current level
        curr = root 
        
        while curr:
            # dummy node to keep track of the start of the next level
            dummy = Node(0)
            # tail node to build the next level's linked list
            tail = dummy
            
            # Iterate through all nodes on the current level
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                
                # Move to the next node in the current level
                curr = curr.next
            
            # Move down to the next level using the dummy's next pointer
            curr = dummy.next
            
        return root
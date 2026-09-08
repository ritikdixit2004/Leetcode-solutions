class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # If the current node is None, there is no path
        if not root:
            return False
        
        # If it is a leaf node, check if the remaining targetSum equals the node's value
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Subtract the current node's value from the targetSum for the next level
        remaining_sum = targetSum - root.val
        
        # Recursively check the left and right subtrees
        return (self.hasPathSum(root.left, remaining_sum) or 
                self.hasPathSum(root.right, remaining_sum))
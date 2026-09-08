class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        def dfs(node, current_sum, path):
            if not node:
                return
            
            # Add current node to the path
            path.append(node.val)
            current_sum -= node.val
            
            # Check if it's a leaf node and the target sum is reached
            if not node.left and not node.right and current_sum == 0:
                res.append(list(path))  # Append a copy of the path
            else:
                # Continue DFS on left and right children
                dfs(node.left, current_sum, path)
                dfs(node.right, current_sum, path)
                
            # Backtrack: remove the current node before going back up the tree
            path.pop()
            
        dfs(root, targetSum, [])
        return res
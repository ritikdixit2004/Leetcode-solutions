class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.max_sum = 0
        def post_order(node):
            if not node:
                return (True, float('inf'), float('-inf'), 0)
            left_is_bst, left_min, left_max, left_sum = post_order(node.left)
            right_is_bst, right_min, right_max, right_sum = post_order(node.right)
            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                current_sum = node.val + left_sum + right_sum
                self.max_sum = max(self.max_sum, current_sum)
                return (True, min(left_min, node.val), max(right_max, node.val), current_sum)
            return (False, 0, 0, 0)
        post_order(root)
        return self.max_sum
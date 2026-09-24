class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res = []
        
        def backtrack(start_num, current_sum, path):
            # Base case: if we have k numbers and the sum is n, add to results
            if len(path) == k and current_sum == n:
                res.append(path[:])
                return
            
            # Pruning: stop exploring if we exceed the required length or sum
            if len(path) >= k or current_sum >= n:
                return
            
            # Try numbers from start_num to 9
            for i in range(start_num, 10):
                path.append(i)
                # Move to the next number (i + 1) to ensure uniqueness
                backtrack(i + 1, current_sum + i, path)
                path.pop() # Backtrack
                
        backtrack(1, 0, [])
        return res
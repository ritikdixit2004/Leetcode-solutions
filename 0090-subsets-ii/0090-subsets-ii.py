class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        # Sorting is crucial to easily skip duplicates
        nums.sort()
        
        def backtrack(start, path):
            # Append a copy of the current path to the results
            res.append(path[:])
            
            for i in range(start, len(nums)):
                # Skip duplicate elements to prevent duplicate subsets
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                # Include the element and move forward
                path.append(nums[i])
                backtrack(i + 1, path)
                
                # Backtrack: remove the element to try the next one
                path.pop()
                
        backtrack(0, [])
        return res
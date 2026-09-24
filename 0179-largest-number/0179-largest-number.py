class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        from functools import cmp_to_key
        
        # Convert integers to strings for concatenation
        nums_str = [str(num) for num in nums]
        
        # Define a custom comparator function
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            elif n1 + n2 < n2 + n1:
                return 1
            else:
                return 0
                
        # Sort the strings using the custom comparator
        nums_str.sort(key=cmp_to_key(compare))
        
        # Join the sorted array into a single string
        largest_num = "".join(nums_str)
        
        # Handle the edge case where the array contains only zeros (e.g., [0, 0])
        if largest_num[0] == "0":
            return "0"
            
        return largest_num
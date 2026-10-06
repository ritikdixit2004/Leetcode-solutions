class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            
            # If the element to the right is larger, a peak must lie to the right
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                # mid could be the peak or the peak lies to the left
                right = mid

        # left == right points to a peak element
        return left
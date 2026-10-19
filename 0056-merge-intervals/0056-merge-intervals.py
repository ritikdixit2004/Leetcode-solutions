class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # Sort intervals by their start values
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        for interval in intervals:
            # If merged is empty or current interval does not overlap with the previous
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Overlap detected: merge by updating the end boundary
                merged[-1][1] = max(merged[-1][1], interval[1])
                
        return merged
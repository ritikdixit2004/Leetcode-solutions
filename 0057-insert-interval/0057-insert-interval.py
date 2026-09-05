class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range(len(intervals)):
            # If the new interval is completely before the current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            # If the new interval is completely after the current interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
                
            # If the intervals overlap, merge them into newInterval
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]), 
                    max(newInterval[1], intervals[i][1])
                ]
                
        # If we loop through everything, append the newInterval at the end
        res.append(newInterval)
        
        return res
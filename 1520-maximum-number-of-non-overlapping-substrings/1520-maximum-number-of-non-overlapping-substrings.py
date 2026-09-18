class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # 1. Record the first and last occurrence of each character
        first = {}
        last = {}
        for i, char in enumerate(s):
            if char not in first:
                first[char] = i
            last[char] = i

        def get_valid_range(i):
            left, right = i, last[s[i]]
            j = left
            while j <= right:
                char = s[j]
                # If a character inside our range started before our current 'left', 
                # this interval is invalid (it will be covered by that earlier character).
                if first[char] < left:
                    return -1, -1
                # Extend the right boundary if the current character appears later
                right = max(right, last[char])
                j += 1
            return left, right

        valid_intervals = []
        for i in range(len(s)):
            # 2. Only check ranges starting at the first occurrence of a character
            if i == first[s[i]]:
                new_left, new_right = get_valid_range(i)
                if new_left != -1:
                    valid_intervals.append((new_left, new_right))

        # 3. Sort intervals by their end points (Greedy approach)
        valid_intervals.sort(key=lambda x: x[1])
        
        res = []
        prev_right = -1
        
        # 4. Pick non-overlapping intervals ending as early as possible
        for left, right in valid_intervals:
            if left > prev_right:
                res.append(s[left:right + 1])
                prev_right = right
                
        return res
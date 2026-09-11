class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # If the combined lengths don't match s3, it's impossible.
        if len(s1) + len(s2) != len(s3):
            return False
        
        # We only need 1D DP array to keep track of the previous row's state
        # to achieve O(s2.length) space complexity.
        dp = [False] * (len(s2) + 1)
        
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    # Both strings are empty
                    dp[j] = True
                elif i == 0:
                    # Only characters from s2 are used
                    dp[j] = dp[j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0:
                    # Only characters from s1 are used
                    dp[j] = dp[j] and s1[i-1] == s3[i+j-1]
                else:
                    # Check if the current character matches s1's or s2's character
                    # dp[j] represents the cell above (using s1)
                    # dp[j-1] represents the cell to the left (using s2)
                    dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1])
                    
        return dp[len(s2)]
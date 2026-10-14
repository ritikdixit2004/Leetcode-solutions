class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: empty string
        
        # Optimization: track max word length to avoid unnecessary substring checks
        max_len = max(len(w) for w in wordDict) if wordDict else 0
        
        for i in range(1, n + 1):
            # Only look back up to the length of the longest word in wordDict
            for j in range(max(0, i - max_len), i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
                    
        return dp[n]
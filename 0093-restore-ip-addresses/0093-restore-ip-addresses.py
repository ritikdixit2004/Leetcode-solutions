class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        # A valid IP address string must be between 4 and 12 characters
        if len(s) < 4 or len(s) > 12:
            return res
            
        def backtrack(i, dots, currentIP):
            # Base case: if we have 4 segments and reached the end of the string
            if dots == 4 and i == len(s):
                res.append(currentIP[:-1])  # Remove the trailing dot and add to results
                return
            
            # If we've placed 4 dots but haven't reached the end of the string, stop exploring
            if dots == 4:
                return
            
            # Try segment lengths of 1, 2, and 3
            for j in range(i, min(i + 3, len(s))):
                segment = s[i:j+1]
                
                # A segment is valid if it's <= 255 and doesn't have leading zeros 
                # (unless it's exactly just "0")
                if int(segment) <= 255 and (len(segment) == 1 or segment[0] != '0'):
                    backtrack(j + 1, dots + 1, currentIP + segment + ".")
                    
        backtrack(0, 0, "")
        
        return res
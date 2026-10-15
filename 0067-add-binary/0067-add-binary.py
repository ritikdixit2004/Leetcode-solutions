class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1

            # Append current bit (total % 2) and update carry (total // 2)
            res.append(str(total % 2))
            carry = total // 2

        # Reverse the collected bits to get the final binary string
        return "".join(reversed(res))
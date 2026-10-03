class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        path = []

        def backtrack(start: int):
            # Base case: valid combination found
            if len(path) == k:
                res.append(path.copy())
                return

            # Pruning optimization:
            # We still need (k - len(path)) elements.
            # If the remaining available elements (from i to n) are fewer than needed, stop.
            # That means i can go at most up to: n - (k - len(path)) + 1
            max_start = n - (k - len(path)) + 1
            for num in range(start, max_start + 1):
                path.append(num)
                backtrack(num + 1)
                path.pop()  # Backtrack

        backtrack(1)
        return res
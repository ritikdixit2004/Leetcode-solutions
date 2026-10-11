class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()  # Sorting enables early stopping (pruning)

        def backtrack(start: int, current_sum: int, path: list[int]):
            if current_sum == target:
                res.append(path.copy())
                return

            for i in range(start, len(candidates)):
                # If adding candidates[i] exceeds target, no subsequent candidate will fit
                if current_sum + candidates[i] > target:
                    break

                path.append(candidates[i])
                # Note: pass 'i' as start index (not i + 1) because elements can be reused
                backtrack(i, current_sum + candidates[i], path)
                path.pop()  # Backtrack

        backtrack(0, 0, [])
        return res
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def make_combination(idx, comb, total):
            # If the current sum equals the target, add the combination to the result
            if total == target:
                res.append(comb[:])
                return
            
            # If the current sum exceeds the target or we've used all candidates, return
            if total > target or idx >= len(candidates):
                return
            
            # Include the current candidate and recurse
            comb.append(candidates[idx])
            make_combination(idx, comb, total + candidates[idx])  # Not incrementing idx allows duplicates
            
            # Backtrack by removing the last element and move to the next candidate
            comb.pop()
            make_combination(idx + 1, comb, total)  # Move to the next candidate

            return res

        return make_combination(0, [], 0)

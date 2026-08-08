class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res, sol = [], []
        sortedc = sorted(candidates)

        def backtrack(i):
            
            if sum(sol) == target:
                res.append(sol[:])
                return
            if i == n or sum(sol) > target:
                return

            for j in range(i, len(candidates)):
                if j > i and sortedc[j] == sortedc[j - 1]:
                    continue

                sol.append(sortedc[j])
                backtrack(j+1)
                sol.pop()
        
        backtrack(0)
        return res
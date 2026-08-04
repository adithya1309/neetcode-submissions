class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        s = []

        for i in range(n-1, -1, -1):
            while s and temperatures[s[-1]] <= temperatures[i]:
                s.pop()
            result[i] = 0 if not s else s[-1] - i
            s.append(i)
        return result





            

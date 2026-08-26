class Solution:
    def calPoints(self, operations: List[str]) -> int:
        n = len(operations)
        ops = ["+", "D", "C"]
        sumstack = []

        for i in range(n):
            item = operations[i]
            if item in ops:
                if item == '+':
                    num1 = sumstack[-1]
                    num2 = sumstack[-2]
                    sumstack.append(num1 + num2)
                elif item == 'D':
                    num = sumstack[-1]
                    num *= 2
                    sumstack.append(num)
                elif item == "C":
                    sumstack.pop()
            else:
                sumstack.append(int(item))
        
        return sum(sumstack)
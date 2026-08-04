class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ('+', '-', '*', '/')
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                i = stack.pop()
                j = stack.pop()

                if token == '+':
                    result = j + i
                elif token == '-':
                    result = j - i
                elif token == '*':
                    result = j * i
                elif token == '/':
                    result = int(j / i)
                stack.append(result)
        return stack.pop()
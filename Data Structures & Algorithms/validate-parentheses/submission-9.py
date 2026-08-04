class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack=[]
        for char in s:
            if char in pairs:
                if len(stack) == 0:
                    return False

                compare = stack.pop()
                if compare != pairs[char]:
                    return False
            
            else:
                stack.append(char)
        
        return len(stack) == 0
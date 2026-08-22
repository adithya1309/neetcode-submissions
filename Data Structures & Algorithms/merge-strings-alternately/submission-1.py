class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer1, pointer2 = 0,0
        n1, n2 = len(word1), len(word2)
        result = []

        while pointer1 < n1 and pointer2 < n2:
            result.append(word1[pointer1])
            result.append(word2[pointer2])
            pointer1 += 1
            pointer2 += 1
        
        result.append(word1[pointer1:])
        result.append(word2[pointer2:])

        return "".join(result)



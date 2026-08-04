class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst = []
        seen ={}
        for string in strs:
            sortedWord = ''.join(sorted(string))
            if sortedWord in seen:
                seen[sortedWord].append(string)
            else:
                seen[sortedWord] = [string]

        return list(seen.values())
                

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs[0])
        a =""
        for i in range(n):
            ch = strs [0][i]
            for j in strs:
                if  i >= len(j) or ch != j [i]:
                    return a
            a += ch
        return a

      
        
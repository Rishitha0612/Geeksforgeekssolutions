class Solution:
    def lastIndex(self, s: str) -> int:
        a=-1
        for i in range(len(s)):
            if s[i]=='1':
                a=i  
        return a 

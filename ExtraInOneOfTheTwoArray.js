class Solution:
    def findExtra(self, a, b):
        for i in range(0,len(b)):
            if(a[i]!=b[i]):
                return i
        if(i<len(a)):
            return len(a)-1
            

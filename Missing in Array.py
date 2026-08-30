class Solution:
    def missingNum(self, arr):
        n=max(arr)
        arr.sort()
        if (len(arr)==max(arr)):
            return max(arr)+1
        for i in range (1,n+1):
            if(i==arr[i-1]):
                continue
            else:
                return i
                
        

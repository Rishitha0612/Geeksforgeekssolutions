class Solution:
    def getMinMax(self, arr):
        n=len(arr)
        if n==1:
            return [arr[0],arr[0]]
        x=arr[0]
        y=arr[0]
        for i in range(0,n):
            if arr[i]>=x:
                x=arr[i]
            if arr[i]<=y:
                y=arr[i]
        return [y,x]        
        

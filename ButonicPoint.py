class Solution:

    def findMaximum(self, arr):
        # code here
        for i in range(len(arr)-1):
            if(arr[i]>arr[i+1]):
                return arr[i]
        return arr[-1]       

class Solution:
    def leaders(self, arr):
         n=len(arr)
         if n==0:
             return []
         max=arr[-1]
         lst=[max]
         for i in range(n-2,-1,-1):
             if arr[i]>=max:
                 max=arr[i]
                 lst.append(max)
         lst.reverse()
         return lst

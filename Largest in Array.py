class Solution:
    def largest(self, arr):
       n=len(arr)
       if n==1:
           return arr[0]
       x=arr[0]
       for i in range(0,n):
           if arr[i]>=x:
               x=arr[i]
       return x           
               
        

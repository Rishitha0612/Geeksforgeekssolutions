class Solution:
    def findDuplicates(self, arr):
       ret=[]
       arr.sort()
       for i in range (1,len(arr)):
           if(arr[i-1]==arr[i]):
               ret.append(arr[i])
       return ret 

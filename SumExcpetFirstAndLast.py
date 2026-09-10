class Solution:
    def sumExceptFirstLast(self,arr):
        # code here
        if(len(arr)==2):
            return 0
        sum1=arr[0]+arr[-1]    
        sum=0
        for i in arr:
            sum=sum+i
        sum1=sum-sum1
        return sum1
            
        
        

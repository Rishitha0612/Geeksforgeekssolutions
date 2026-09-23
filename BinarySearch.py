class Solution:
    def binarySearch(self, arr, k):
        # code here
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if(k>arr[mid]):
                low=mid+1
            elif(k==arr[mid]):
                return True
            else:
                high=mid-1
               
        return False 

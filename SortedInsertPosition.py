class Solution:
    def searchInsertK(self, arr, k):
        
        for i in range(len(arr)):
            if arr[i] >= k:
                return i

        return len(arr)

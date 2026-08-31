class Solution:
    def rotate(self, arr):
        n=arr[0]
        arr[0]=arr[len(arr)-1]
        arr.pop()
        arr.insert(1,n)
        return arr 

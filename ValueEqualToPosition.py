class Solution:
    def valEqualToPos(self, arr):
        lst=[]
        for i in range(len(arr)):
            if(i+1==arr[i]):
                lst.append(i+1)
        return lst        
        

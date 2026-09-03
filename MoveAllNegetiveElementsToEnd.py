class Solution:
    def segregateElements(self, arr):
        lst1=[]
        lst2=[]
        for i in range(len(arr)):
            if(arr[i]>=0):
                lst1.append(arr[i])
            else:
                lst2.append(arr[i])
        arr.clear()
        arr.extend(lst1)
        arr.extend(lst2)
        return arr

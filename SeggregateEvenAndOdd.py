class Solution:

    def segregateEvenOdd(self,arr):
        # code here
        lst1=[]
        lst2=[]
        lst=[]
    
        for v in arr:
            if(v%2==0):
                lst1.append(v)
            else:
                lst2.append(v)
        lst1.sort()
        lst2.sort()
        for i in lst1:
            lst.append(i)
        for i in lst2:
            lst.append(i)
            
        arr[:]=lst
        return arr
    
        
            
        

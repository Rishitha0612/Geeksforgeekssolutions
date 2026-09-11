class Solution:
    def convertFive(self, n):
        # code here
        if(n==0):
            return 5
        sum=n
        p=1
        while(n>0):
            
                x=n%10
                n=n//10
                if(x==0):
                   sum=sum+p*5 
                
                else:
                   sum=sum+0  
                p=p*10  
        return sum     

'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''


class Solution:

    def getNode(self, head: 'Node', k: int) -> int:
        """ code here """
        c=0
        j=head
        while(j!=None):
            c=c+1
            j=j.next
        if k>c:
            return -1
        count=1
        i=head
        while i!=None and count!=k:
            count+=1
            i=i.next
        return i.data    
            

#class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None


class Solution:
    def isCircular(self, head):
        # code here
        i=head
        while i.next!=head:
            if(i.next==None):
                return False
            i=i.next
        return True    
            

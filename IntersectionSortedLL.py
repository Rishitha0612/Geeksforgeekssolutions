'''Structure of a Linked list Node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

'''
class Solution:
    def findIntersection(self,head1,head2):
        if head1 is None:
            return head1
        if head2 is None:
            return head2
        s=set()
        i=head1
        j=head2
        dummy=Node(0)
        k=dummy
        
            
        while i!=None:
            if i.data not in s:
                s.add(i.data)
            i=i.next 
        while j!=None:
            if j.data in s:
               new_node = Node(j.data)
               k.next = new_node
               k= new_node
            j=j.next
        return dummy.next  
                
                
        

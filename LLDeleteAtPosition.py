''' Structure of Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def deleteNode(self, head, x):
        if head is None:
            return None
        if x==1:
            return head.next
        count=1
        prev=head
        i=head.next
        while i!=None:
            count+=1
            if count==x:
                prev.next=i.next
            prev=i
            i=i.next
            
        return head        
        

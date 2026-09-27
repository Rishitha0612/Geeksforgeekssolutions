class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def insertAtEnd(self, head, x):
        b=Node(x)#code here 
        i=head
        if head==None:
            head=b
            return head
        while i.next!=None:
            i=i.next
        i.next=b   
        b.next=None
        return head

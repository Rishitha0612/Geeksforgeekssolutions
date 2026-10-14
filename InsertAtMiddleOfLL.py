'''
structure of a linked list node 
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def insertInMiddle(self, head, x):
        #code here
        new_node=Node(x)
        count=0
        i=head
        if head==None:
            head=new_node

            return head

        
        while i!=None:
            count+=1
            i=i.next
        j=head
        index=(count+1)//2
        for _ in range (index-1):
            j=j.next
            
        new_node.next=j.next 
        j.next=new_node
        
        
    
        
        return head

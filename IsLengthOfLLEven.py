"""
structure of link list node
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
        
"""    
class Solution:
    
    def isEven(self, head):
        # Code here
        count=0
        i=head
        while i!=None:
            count=count+1
            i=i.next
        if count%2==0:
            return True
        return False 

'''Structure of Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def searchKey(self, head, key):
        # Code here
        i=head
        while i!=None:
            if i.data==key:
                return True
            i=i.next
        return False    

''' Linked List Node Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def getLength(self, head):
        # code here
        count=1
        i=head
        while i.next!=head:
            count+=1
            i=i.next
        return count    

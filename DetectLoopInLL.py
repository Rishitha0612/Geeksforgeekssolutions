''' Linked List Node Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def detectLoop(self, head):
        # code here
        i=head
        j=head
        while i and i.next:
            j=j.next
            i=i.next.next
            if i==j:
                return True
        return False 

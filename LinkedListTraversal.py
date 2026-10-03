"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    def printList(self, head):
        # code here
       
        i=head
        while i!=None:
            print(i.data,end=" ")
            i=i.next
            

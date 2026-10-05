""" Structure of linked list Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Initially, the next pointer is None.
 """ 
class Solution:
    def insertIntoEmpty(self, last, data):
        # code here
        head=Node(data)
        head.next=head
        last=head
        return last

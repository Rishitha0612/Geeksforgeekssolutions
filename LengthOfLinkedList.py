''' Structure of linked list Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def getCount(self, head):
        # code here
        count=0
        i=head
        if i==None:
            return 0
        while i!=None:
            i=i.next
            count=count+1
        return count 

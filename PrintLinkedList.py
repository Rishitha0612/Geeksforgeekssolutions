'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''

class Solution:
    def printList(self, head):
        # code here
        lst=[]
        i=head
        while i!=None:
            lst.append(i.data)
            i=i.next
        return lst    

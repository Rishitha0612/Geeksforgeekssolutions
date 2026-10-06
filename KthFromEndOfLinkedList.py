""" Structure of Linked List Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
"""

class Solution:
    def getKthFromLast(self, head, k):
        # code here
        i=head
        lst=[]
        while i!=None:
            lst.append(i.data)
            i=i.next
            
        n=len(lst)
        if k>n:
            return -1
        return lst[n-k]

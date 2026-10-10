''' Structure of linked list Node
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
class Solution:
    def removeDuplicates(self, head):
        # code here
      if head is None:
            return head    
      s=set()
      s.add(head.data)
      prev=head
      i=head.next
      while i!=None:
          if i.data in s:
              prev.next=i.next
          else:
             s.add(i.data)
             prev=i
          i=i.next
      return head      

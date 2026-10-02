''' Structure of doubly linked list Node
  class Node:
      def __init__(self, x):
          self.data = x
          self.next = None
          self.prev = None
'''
class Solution:
    def displayList(self, head):
        # code here
        lst=[]
        lst1=[]
        i=head
        while i!=None:
            lst.append(i.data)
            i=i.next
        lst1=lst[::-1]
        return [lst,lst1]
        
            

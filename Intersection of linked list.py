# structure of list node:
# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.next = None

class Solution:
    def findIntersection(self, head1, head2):
        # code here
        if head1 is None:
           return head1
        if head2 is None:
            return head2
        s=set()
        i=head2
        j=head1
        dummy=Node(0)
        k=dummy


        while i!=None:
            if i.data not in s:
                s.add(i.data)
            i=i.next 
        while j!=None:
            if j.data in s:
                new_node = Node(j.data)
                k.next = new_node
                k= new_node
            j=j.next
        return dummy.next         

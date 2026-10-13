''' Structure of linked list Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def pairwiseSwap(self, head):
        if head is None or head.next is None:
            return head

        # New head will be the second node
        new_head = head.next

        prev = None
        curr = head

        while curr is not None and curr.next is not None:
            next_node = curr.next
            next_pair = next_node.next

            # Swap the pair
            next_node.next = curr
            curr.next = next_pair

            # Connect previous pair to current swapped pair
            if prev is not None:
                prev.next = next_node

            prev = curr
            curr = next_pair

        return new_head
        # code here
        
            
            
            
        

                 
            

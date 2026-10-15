""" Node Structure
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
"""

class Solution:
    def deleteMid(self, head):
        # code here
        if head==None:
            return None
        if head.next==None:
            return None
        count=0
        midcount=0
        i=head
        prev=head
        while i!=None:
            count+=1
            i=i.next
        j=head.next
        while j!=None:
            midcount+=1
            if(midcount==count//2):
                prev.next=j.next
            prev=j
            j=j.next
        return head    
                
                
            
            

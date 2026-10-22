'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def isPalindrome(self, head):
        # code here
        i=head
        lst=[]
        while i!=None:
            lst.append(i.data)
            i=i.next
        lst1=lst[::-1]
        if(lst==lst1):
            return True
        else:
            return False
        

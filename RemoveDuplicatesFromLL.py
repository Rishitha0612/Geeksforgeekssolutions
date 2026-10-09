''' Structure of linked list Node
    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }
'''
def removeDuplicates(head):
    i = head

    while i != None and i.next != None:
        if i.data == i.next.data:
            i.next = i.next.next
        else:
            i = i.next

    return head       

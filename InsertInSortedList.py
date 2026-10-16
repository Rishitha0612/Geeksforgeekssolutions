class Solution:
    def sortedInsert(self, head, key):
        new_node = Node(key)

        # Empty list OR insert before head
        if head is None or key <= head.data:
            new_node.next = head
            return new_node

        curr = head

        # Find the node after which we insert
        while curr.next is not None and curr.next.data < key:
            curr = curr.next

        new_node.next = curr.next
        curr.next = new_node

        return head

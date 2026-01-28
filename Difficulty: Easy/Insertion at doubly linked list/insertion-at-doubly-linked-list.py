class Solution:
    def insertAtPos(self, head, p, x):
        new_node = Node(x)
        curr = head
        count = 0

        # Traverse to (p-1)th node
        while curr.next and count < p:
            curr = curr.next
            count += 1

        # If position is out of bounds
        if curr is None:
            return head

        # Insert in between or at end
        new_node.next = curr.next
        new_node.prev = curr

        if curr.next:
            curr.next.prev = new_node

        curr.next = new_node

        return head

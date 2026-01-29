class Node:
    def __init__(self, d):
        self.data = d
        self.prev = None
        self.next = None

class Solution:
    def delPos(self, head, x):
        # Case 1: List is empty or invalid position
        if not head or x < 1:
            return head
        
        temp = head
        
        # Case 2: Deleting the Head (Position 1)
        if x == 1:
            head = head.next
            if head:
                head.prev = None
            return head
        
        # Traverse to the node at position x
        count = 1
        while temp is not None and count < x:
            temp = temp.next
            count += 1
            
        # Case 3: Position x is greater than number of nodes
        if temp is None:
            return head
        
        # Case 4: Deleting Middle or Tail node
        # Adjust the 'next' pointer of the previous node
        if temp.prev:
            temp.prev.next = temp.next
            
        # Adjust the 'prev' pointer of the next node (if it exists)
        if temp.next:
            temp.next.prev = temp.prev
            
        return head
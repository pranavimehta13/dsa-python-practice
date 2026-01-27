#User function Template for python3


# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
	   self.data = data
	   self.next = None
	   self.prev = None

class Solution:
    def constructDLL(self, arr):
        head = None
        for i in range(len(arr)):
            new_node = Node(arr[i])
            if not head:
                head = new_node
                curr = head
                continue
            curr.next = new_node
            new_node.prev = curr
            curr = curr.next
        return head
        
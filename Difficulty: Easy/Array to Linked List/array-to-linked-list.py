class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def arrayToList(self, arr):
        head = None
        for i in range(len(arr)):
            new_node = Node(arr[i])
            if head == None:
                head = new_node
                curr = new_node
            curr.next = new_node
            curr = curr.next
        return head
            
            
        
        
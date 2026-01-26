
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

class Solution:
    def getCount(self, head):
        curr = head
        count = 0
        while curr != None:
            curr = curr.next
            count+=1
        return count
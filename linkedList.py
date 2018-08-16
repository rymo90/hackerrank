class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")

            current = current.next

    def insert(self, data):
        nyNode = Node(data)
        if self.head == None:
            self.head = nyNode
        else:
            current = self.head
            while(current.next is not None):
                current = current.next
            current.next = nyNode
        return self.head


mylist = Solution()
T = int(input())
for i in range(T):
    data = int(input())
    mylist.insert(data)
mylist.display()

import sys


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.insert(0, data)

    def dequeue(self):
        return self.queue.pop()


class Stack:
    def __init__(self):
        self.stack = []

    def add(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()


class Solution:
    def __init__(self):
        self.stack = Stack()
        self.queue = Queue()

    def pushCharacter(self, data):
        self.stack.add(data)

    def enqueueCharacter(self, data):

        self.queue.enqueue(data)

    def popCharacter(self):
        return self.stack.pop()

    def dequeueCharacter(self):
        return self.queue.dequeue()


s = input()
l = len(s)
obj = Solution()
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
isPalindrome = True

for i in range(l//2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")

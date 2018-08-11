class Queue:
    def __init__(self):
        self.queue = list()
    def enqueue(self,data):
        if data not in self.queue:
            self.queue.insert(0,data)
            return True
        else:
            return False
    def dequeue(self):
        return self.queue.pop(0)
    def size(self):
        return len(self.queue)
    def printQueue(self):
        return self.queue
n= int(input())
alphabet= "abcdefghijklmnopqrstuvwxyz"
alphabet = alphabet[:n]
alphabet=alphabet[::-1]
width= ((n-1)*4)+1
column= (n*2)-1
left = ""
right=""
pattern = ""
myQueue= Queue()
for i in range(column):
    if i < n:
        pattern= left+alphabet[i]+right
        print(pattern.center(width,"-"))
        left+= alphabet[i]+"-"
        right= left[::-1]
        if i+1 < n:
            myQueue.enqueue(pattern)
    else:
        pattern= myQueue.dequeue()
        print(pattern.center(width, "-"))

class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        if root == None:
            return 0
        else:
            dr = self.getHeight(root.right)
            dl = self.getHeight(root.left)
            if dr > dl:
                return dr+1
            else:
                return dl+1


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height-1)

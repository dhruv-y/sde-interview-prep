'''
Description => Given a sorted (increasing order) array with unique integer elements, write an
algorithm to create a binary search tree with minimal height.

Approach: 
    - Keep maintaining L and R subtree somewhat equally
    - Split at each mid point recursively?
    - Set root = mid & keep recursing
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root = None):
        self.root = root

    def addNode(self, val):
        node = Node(val, )
        if not self.root:
            self.root
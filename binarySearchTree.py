"""
A binary tree is a linked data structure where each nodes points to at most 2 child nodes.
Nodes with no children are leaf nodes.

The depth of a node is the number of nodes from root to the node, with root having depth
of 0.
The height of a node is the number of nodes on the path from the node to the deepest leaf.
Count from the node and up towards the root.
Height of the tree is the maximum height of any node in the tree.

Binary Search Tree is a binary tree to help search data in the tree where the nodes greater
than the root is on the right and nodes less than the root is on the right.
"""

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
   
  def insert(self, data):
    if self.data = data: # duplicate
      return False
    elif data < self.data:
      if self.left:
        return self.left.insert(data)
      else:
        self.left = Node(data)
        return True
    else:
      if self.right:
        return self.right.insert(data)
      else:
        self.right = Node(data)
        return True
  
  def find(self, target):
    if self.data == target:
      return True
    elif target < self.data and self.left:
      return self.left.find(target)
    elif target > self.data and self.right:
      return self.right.find(target)
    return False

class BST:
  def __init__(self):
    self.root = None
    
  def insert(self, data): 
    if self.root:
      return self.root.insert(data)
    else: 
      self.root = Node(data)
      return True
   
  def find(self, target):
    if self.root:
      return self.root.find(target)
    else:
      return False
  
    
  

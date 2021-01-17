# O(n) time | O(d) where d is the depth of the tree

def invertBinaryTree(tree):
    if tree == None:
	    return
    tmp = tree.left
    tree.left = tree.right
    tree.right = tmp
	
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)
	


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
		
def calculateDepth(root, depth, sums) -> None:
	if root == None:
		return 0
	
	sums.append(depth)
		
	calculateDepth(root.left, depth + 1, sums)
	calculateDepth(root.right, depth + 1, sums)
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root) -> list:
    sums = []
    calculateSum(root, 0, sums)
    return sums

def calculateSum(root, currSum: float, sums: list):
    if root == None:
        return

    currSum += root.value
    if root.left == None and root.right == None:
        return currSum

    calculateSum(root.left, currSum, sums)
    calculateSum(root.right, currSum, sums)

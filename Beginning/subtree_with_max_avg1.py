"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """

    def findSubtree2(self, root):
        # write your code here
        node, _, _ = self.findSubtreewValue(root)
        return node

    def findSubtreewValue(self, root):

        if (root.left == None):
            if (root.right == None):
                return (root, root.val, 1)
            else:
                rightNode, rightAve, rightNum = self.findSubtreewValue(root.right)
                if (root.val > rightAve):
                    return [root, (rightAve * rightNum + root.val) / (rightNum + 1), rightNum + 1]
                else:
                    return rightNode, rightAve, rightNum
        else:
            if (root.right == None):
                leftNode, leftAve, leftNum = self.findSubtreewValue(root.left)
                if (root.val > leftAve):
                    return [root, (leftAve * leftNum + root.val) / (leftNum + 1), leftNum + 1]
                else:
                    return leftNode, leftAve, leftNum
            else:
                rightNode, rightAve, rightNum = self.findSubtreewValue(root.right)
                leftNode, leftAve, leftNum = self.findSubtreewValue(root.left)
                aveList = [root.val, leftAve, rightAve]
                maxIndex = aveList.index(max(aveList))

                if (maxIndex == 0):
                    [root, (leftAve * leftNum + rightAve * rightNum + root.val) / (leftNum + rightNum + 1),
                     leftNum + rightNum + 1]
                elif (maxIndex == 1):
                    return leftNode, leftAve, leftNum
                else:
                    return rightNode, rightAve, rightNum
'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Question1: Subtree with Maximum Average
Given the root of a 'binary tree', find the subtree with maximum average. Return the root of the subtree.
A subtree of a tree is any node of that tree plus all its descendants. The average value of a subtree is the sum of its values, divided by the number of nodes.
Example:
Input:
                  5
               /     \
              6      1
Output: 6.00000
Explanation:
For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
For the node with value = 6 we have an average of 6 / 1 = 6.
For the node with value = 1 we have an average of 1 / 1 = 1.
So the answer is 6 which is the maximum.
*** Also try modified version:
Everything same except for the definition of Subtree.
A subtree of a tree is the node which have at least 1 child plus all its descendants.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Question2: Subtree with Maximum Average
Given the root of a 'M-ary tree', find the subtree with maximum average. Return the root of the subtree.
A subtree of a tree is any node of that tree plus all its descendants. The average value of a subtree is the sum of its values, divided by the number of nodes.
Example 1:
Input:
                          1
                  /       |        \
               -5       13        4
              /   \     /  \
             1   2   4   -2
Output: 13.00000
Explanation: For the node with value = 13 we have an average of (13 + 4 + -2) / 3 = 5 which is the maximum.
*** Also try modified version:
Everything same except for the definition of Subtree.
A subtree of a tree is the node which have at least 1 child plus all its descendants.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''


# Question 1 - Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # this function can return maximum average subtree as well as maximum average value
    def MaximumAverageSubtree(self, root):
        '''
        >>> solution = Solution()
        >>> solution.MaximumAverageSubtree(Node1)
        14
        >>> solution.MaximumAverageSubtree(Node11)
        20
        '''
        # if given tree only has None node
        if root.val == None: return None
        # in case node contains negative value
        self.maxAverage = float('-inf')
        self.maxNode = None

        def helper(node):
            if not node: return 0, 0.0
            leftTotal, leftSum = helper(node.left)
            rightTotal, rightSum = helper(node.right)

            currentTotal = 1 + leftTotal + rightTotal
            currentSum = node.val + leftSum + rightSum

            currentAverage = currentSum / currentTotal
            if currentAverage > self.maxAverage:
                self.maxAverage = currentAverage
                self.maxNode = node
            return currentTotal, currentSum

        helper(root)
        # for submission, return 'self.maxNode' instead
        return self.maxNode.val

    # ------------------------------------------------------------------------------------------

    # modified version
    def MaximumAverageSubtree2(self, root):
        '''
        >>> solution2 = Solution()
        >>> solution2.MaximumAverageSubtree2(Node1)
        14
        >>> solution2.MaximumAverageSubtree2(Node11)
        14
        '''
        # if given tree only has None node
        if root.val == None: return None
        # in case node contains negative value
        self.maxAverage = float('-inf')
        self.maxNode = None

        def helper(node):
            if not node: return 0, 0.0
            leftTotal, leftSum = helper(node.left)
            rightTotal, rightSum = helper(node.right)

            currentTotal = 1 + leftTotal + rightTotal
            currentSum = node.val + leftSum + rightSum

            currentAverage = currentSum / currentTotal
            # checking if it has at least one child
            if (currentAverage > self.maxAverage) and (node.left or node.right):
                self.maxAverage = currentAverage
                self.maxNode = node
            return currentTotal, currentSum

        helper(root)
        # for submission, return 'self.maxNode' instead
        return self.maxNode.val


# example binary tree from https://en.wikipedia.org/wiki/Binary_search_tree
# -----------------------------------------------------------------------------------------------------
Node1 = TreeNode(8)
Node2 = TreeNode(3)
Node3 = TreeNode(10)
Node4 = TreeNode(1)
Node5 = TreeNode(6)
Node6 = TreeNode(4)
Node7 = TreeNode(7)
Node8 = TreeNode(14)
Node9 = TreeNode(13)

Node1.left = Node2
Node1.right = Node3

Node2.left = Node4
Node2.right = Node5
Node5.left = Node6
Node5.right = Node7

Node3.right = Node8
Node8.left = Node9
# -----------------------------------------------------------------------------------------------------
# modified binary tree from above for modified version
Node11 = TreeNode(8)
Node22 = TreeNode(3)
Node33 = TreeNode(10)
Node44 = TreeNode(1)
Node55 = TreeNode(6)
Node66 = TreeNode(4)
Node77 = TreeNode(7)
Node88 = TreeNode(14)
Node99 = TreeNode(20)

Node11.left = Node22
Node11.right = Node33

Node22.left = Node44
Node22.right = Node55
Node55.left = Node66
Node55.right = Node77

Node33.right = Node88
Node88.left = Node99


# -----------------------------------------------------------------------------------------------------

# Question 2 - M-ary tree

# Definition for a M-ary tree node.
class TreeNode2:
    def __init__(self, x):
        self.val = x
        self.children = []

    def add_child(self, child):
        self.children.append(TreeNode2(child))


class Solution2:
    # this function can return maximum average subtree as well as maximum average value
    def MaximumAverageSubtree3(self, root):
        '''
        >>> solution2 = Solution2()
        >>> solution2.MaximumAverageSubtree3(Tnode1)
        15
        '''
        # if given tree only has None node
        if not root: return None
        # in case node contains negative value
        self.maxAverage = float('-inf')
        self.maxNode = None

        def helper(node):
            if not node: return 0, 0.0

            currentTotal = 1
            currentSum = node.val

            for child in node.children:
                childTotal, childSum = helper(child)
                currentTotal += childTotal
                currentSum += childSum

            currentAverage = currentSum / currentTotal
            if (currentAverage > self.maxAverage):
                self.maxAverage = currentAverage
                self.maxNode = node
            return currentTotal, currentSum

        helper(root)
        # for submission, return 'self.maxNode' instead
        return self.maxNode.val

    # ------------------------------------------------------------------------------------------

    # modified version
    def MaximumAverageSubtree4(self, root):
        '''
        >>> solution2 = Solution2()
        >>> solution2.MaximumAverageSubtree4(Tnode1)
        18
        '''
        # if given tree only has None node
        if not root: return None
        # in case node contains negative value
        self.maxAverage = float('-inf')
        self.maxNode = None

        def helper(node):
            # taking 'at least 1 child' into account
            if not node.children: return 1, node.val

            currentTotal = 1
            currentSum = node.val

            for child in node.children:
                childTotal, childSum = helper(child)
                currentTotal += childTotal
                currentSum += childSum

            currentAverage = currentSum / currentTotal
            if (currentAverage > self.maxAverage):
                self.maxAverage = currentAverage
                self.maxNode = node
            return currentTotal, currentSum

        helper(root)
        # for submission, return 'self.maxNode' instead
        return self.maxNode.val


# example m-ary tree from https://leetcode.com/discuss/interview-question/349617
# --------------------------------------------------------------------------------------------------------------
Tnode1 = TreeNode2(20)

Tnode1.add_child(12)
Tnode1.add_child(18)

Tnode1.children[0].add_child(11)
Tnode1.children[0].add_child(2)
Tnode1.children[0].add_child(3)

Tnode1.children[1].add_child(15)
Tnode1.children[1].add_child(8)
# --------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    import doctest

    doctest.testmod()
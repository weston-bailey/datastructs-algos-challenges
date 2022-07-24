# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.stack = []

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.recurse(root)

        print(self.stack)

        for i in range(1, len(self.stack)):
            if self.stack[i] <= self.stack[i - 1]:
                print(self.stack[i], self.stack[i - 1])
                return False

        return True


    def recurse(self, node):
        if not node:
            return None

        self.recurse(node.left)

        self.stack.append(node.val)

        self.recurse(node.right)



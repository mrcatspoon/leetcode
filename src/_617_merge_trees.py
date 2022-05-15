# https://leetcode.com/problems/merge-two-binary-trees/
from typing import Optional


class TreeNode:
    __slots__ = ("val", "left", "right")

    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            root = TreeNode(
                root1.val + root2.val,
                left=self.mergeTrees(root1.left, root2.left),
                right=self.mergeTrees(root1.right, root2.right),
            )
            return root
        else:
            return root1 or root2

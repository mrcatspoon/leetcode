# https://leetcode.com/problems/binary-tree-preorder-traversal/
from typing import List, Optional


class TreeNode:
    __slots__ = ("val", "left", "right")

    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root:
            self.traverse(root, result)
        return result

    def traverse(self, root: Optional[TreeNode], result: List[int]):
        if root.left:
            self.traverse(root.left, result)
        if root.right:
            self.traverse(root.right, result)
        result.append(root.val)

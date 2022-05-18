# https://leetcode.com/problems/maximum-depth-of-binary-tree/
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
    __slots__ = ("_max_depth",)

    def __init__(self):
        self._max_depth = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            self.find_max_depth(root, 1)
        return self._max_depth

    def find_max_depth(self, current: TreeNode, level: int):
        if current.left:
            self.find_max_depth(current.left, level + 1)
        if current.right:
            self.find_max_depth(current.right, level + 1)
        if level > self._max_depth:
            self._max_depth = level

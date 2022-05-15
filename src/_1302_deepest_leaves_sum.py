# https://leetcode.com/problems/deepest-leaves-sum/
from collections import defaultdict
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
    __slots__ = ("_stack", "_deepest_level")

    def __init__(self):
        self._stack = defaultdict(list)
        self._deepest_level = 0

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root.right and not root.left:
            return root.val
        self.build_stack(root, 0)
        return sum(self._stack[self._deepest_level])

    def build_stack(self, current: TreeNode, level: int):
        if current.left:
            self.build_stack(current.left, level + 1)
        if current.right:
            self.build_stack(current.right, level + 1)
        self._stack[level].append(current.val)
        if level > self._deepest_level:
            self._deepest_level = level

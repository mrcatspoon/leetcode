# https://leetcode.com/problems/symmetric-tree/
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if root.left and not root.right:
            return False
        if root.right and not root.left:
            return False

        left_stack = defaultdict(list)
        self.build_stack(root.left, 0, left_stack)

        right_stack = defaultdict(list)
        self.build_stack(root.right, 0, right_stack)

        for level, values in left_stack.items():
            if level not in right_stack:
                return False
            if values != right_stack[level][::-1]:
                return False

        return True

    def build_stack(self, current: TreeNode, level: int, stack: dict):
        stack[level].append(current.val if current else None)
        if current:
            self.build_stack(current.left, level + 1, stack)
            self.build_stack(current.right, level + 1, stack)

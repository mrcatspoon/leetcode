# https://leetcode.com/problems/binary-tree-level-order-traversal/
from collections import defaultdict
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
    __slots__ = ("_stack",)

    def __init__(self):
        self._stack = defaultdict(list)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        self.build_stack(root, 0)
        return list(self._stack.values())

    def build_stack(self, current: TreeNode, level: int):
        self._stack[level].append(current.val)
        if current.left:
            self.build_stack(current.left, level + 1)
        if current.right:
            self.build_stack(current.right, level + 1)

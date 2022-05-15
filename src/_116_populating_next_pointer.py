# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
from collections import defaultdict
from typing import Optional


class Node:
    __slots__ = ("val", "left", "right", "next")

    def __init__(
        self, val: int = 0, left: Optional["Node"] = None, right: Optional["Node"] = None, next: Optional["Node"] = None
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    __slots__ = ("_stack",)

    def __init__(self):
        self._stack = defaultdict(list)

    def connect(self, root: Node) -> Node:
        if not root:
            return root

        self.build_stack(root, 0)
        for level, stack in self._stack.items():
            for i in range(len(stack)):
                try:
                    stack[i].next = stack[i + 1]
                except IndexError:
                    continue

        return root

    def build_stack(self, current: Node, level: int):
        if current.left:
            self.build_stack(current.left, level + 1)
        if current.right:
            self.build_stack(current.right, level + 1)
        self._stack[level].append(current)

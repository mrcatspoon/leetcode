# https://leetcode.com/problems/middle-of-the-linked-list/
from typing import Optional


class ListNode:
    __slots__ = ("val", "next")

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        size = 0
        item = head
        while item:
            size += 1
            item = item.next

        for _ in range(size // 2):
            head = head.next
        return head

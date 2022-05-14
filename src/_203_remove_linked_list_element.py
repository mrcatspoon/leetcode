# https://leetcode.com/problems/remove-linked-list-elements/
from typing import Optional


class ListNode:
    __slots__ = ("val", "next")

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return

        current = prev = head

        while current:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next

        return head.next if head.val == val else head

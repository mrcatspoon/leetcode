# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
from typing import Optional


class ListNode:
    __slots__ = ("val", "next")

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        current = prev = head
        visited = set()
        while current:
            if current.val in visited:
                prev.next = current.next
            else:
                prev = current
            visited.add(current.val)
            current = current.next

        return head

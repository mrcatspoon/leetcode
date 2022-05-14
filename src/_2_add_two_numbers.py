# https://leetcode.com/problems/add-two-numbers/
from typing import Optional, Tuple


class ListNode:
    __slots__ = ("val", "next")

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return

        memory = 0
        results = []
        while l1 or l2 or memory:
            memory, value = self.add(l1, l2, memory)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            results.append(value)

        result = node = ListNode(results[0])
        for value in results[1:]:
            value = ListNode(value)
            node.next = value
            node = value

        return result

    def add(self, l1: Optional[ListNode], l2: Optional[ListNode], memory: int) -> Tuple[int, int]:
        value = l1.val if l1 else 0
        if l2:
            value += l2.val
        if memory:
            value += memory
            memory = 0
        if value >= 10:
            memory = 1
            value -= 10
        return memory, value

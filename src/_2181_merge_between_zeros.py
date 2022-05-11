# https://leetcode.com/problems/merge-nodes-in-between-zeros/
from typing import Optional


class ListNode:
    __slots__ = ("val", "next")

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = head.next
        tmp, results = [], []
        while head:
            if head.val == 0:
                results.append(sum(tmp))
                tmp.clear()
            else:
                tmp.append(head.val)
            head = head.next

        result = node = ListNode(results[0])
        for value in results[1:]:
            value = ListNode(value)
            node.next = value
            node = value

        return result

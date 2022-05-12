from typing import Optional


class ListNode:
    __slots__ = ("val", "next")

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        main_pointer = secondary_pointer = head
        for _ in range(n):
            main_pointer = main_pointer.next
        if not main_pointer:
            return head.next
        while main_pointer.next:
            main_pointer = main_pointer.next
            secondary_pointer = secondary_pointer.next
        secondary_pointer.next = secondary_pointer.next.next
        return head

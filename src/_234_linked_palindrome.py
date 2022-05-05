# https://leetcode.com/problems/palindrome-linked-list/
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values[::-1] == values

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return
        if not list1:
            return list2
        if not list2:
            return list1

        results = []
        while True:
            l1 = list1.val if list1 else None
            l2 = list2.val if list2 else None
            if l1 is None and l2 is None:
                break

            if l1 is None:
                results.append(l2)
                list2 = list2.next if list2 else None
                continue
            elif l2 is None:
                results.append(l1)
                list1 = list1.next if list1 else None
                continue

            if l1 == l2:
                results.append(l1)
                results.append(l2)
                list1 = list1.next if list1 else None
                list2 = list2.next if list2 else None
            elif l1 > l2:
                results.append(l2)
                list2 = list2.next if list2 else None
            else:
                results.append(l1)
                list1 = list1.next if list1 else None

            if not list1 and not list2:
                break

        result = node = ListNode(results[0])
        for value in results[1:]:
            value = ListNode(value)
            node.next = value
            node = value

        return result

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr is not None:
            next_n = curr.next
            curr.next = prev
            prev = curr
            curr = next_n

        return prev

case_1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))

sol = Solution()
sol.reverseList(case_1)
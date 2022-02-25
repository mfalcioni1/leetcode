from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head_1 = l1
        head_2 = l2
        unl_1 = []
        unl_2 = []
        while head_1 or head_2:
            if head_1:
                unl_1.append(head_1.val)
                head_1 = head_1.next
            if head_2:
                unl_2.append(head_2.val)
                head_2 = head_2.next
        val_1 = [str(x) for x in unl_1]
        val_2 = [str(x) for x in unl_2]
        val_1 = int("".join(val_1)[::-1])
        val_2 = int("".join(val_2)[::-1])
        added = str(val_1 + val_2)
        str_res = []
        str_res[:0] = added
        for i in range(len(str_res)):
            if i == 0:
                res = ListNode(val = int(str_res[i]), next = None)
            else:
                tail = res
                res = ListNode(val = int(str_res[i]), next = tail)
        return res


l1 = ListNode(val = 2, next = ListNode(val = 4, next = ListNode(val = 3, next = None)))
l2 = ListNode(val = 5, next = ListNode(val = 6, next = ListNode(val = 4, next = None)))

sol = Solution()
answer = sol.addTwoNumbers(l1=l1, l2=l2)
# [7,0,8]
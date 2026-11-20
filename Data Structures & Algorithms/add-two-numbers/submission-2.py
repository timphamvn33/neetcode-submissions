# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # total = l1.val + l2.val + carry
        # carry = total // 10
        # digit = total % 10

        dummy = ListNode(-1)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            total = l1_val + l2_val + carry

            carry = total // 10
            digit = total % 10

            curr.next = ListNode(digit)

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next
            curr = curr.next
        return dummy.next
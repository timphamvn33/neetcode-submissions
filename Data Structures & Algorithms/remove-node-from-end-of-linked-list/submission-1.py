# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # using the slow fast pattern with the gap n
        dummy = ListNode(-1, head)
        

        slow=dummy
        fast=dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        #will get the node before the nth node
        # get the next node next to node at n
        slow.next = slow.next.next
        return dummy.next


        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        [0, 1, 2, 3]
        [6, 5, 4]
        [0, 1, 2, 3, 4, 5,6]

        # find the mid
        slow, fast = head, head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        # reverse the 2nd list
        mid = slow.next
        slow.next = None
        prev = None

        while mid:
            next = mid.next
            mid.next = prev
            prev = mid
            mid = next
        # join the fist and sec list

        first, sec = head, prev
        while sec:
            next1 = first.next
            next2 = sec.next
            first.next, sec.next = sec, next1
            first = next1
            sec = next2
            

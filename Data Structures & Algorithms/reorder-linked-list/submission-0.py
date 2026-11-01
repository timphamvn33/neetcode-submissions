# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        # find the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the 2nd half
        prev = None
        curr = slow.next
        slow.next = None
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        # merge 2 parts together
        # [0, 1, 2, 3] -> [0, 1, 3, 2] -> [0,3, 1, 2]


        while prev:
            tmp1, tmp2 = head.next, prev.next
            head.next = prev
            prev.next = tmp1
            head, prev = tmp1, tmp2



        


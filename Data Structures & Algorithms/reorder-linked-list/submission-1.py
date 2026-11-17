# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # [0,1,2,3]
        # [6,5,4,3]

        # find the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse half of the list
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # join the 1st half of the list and the reverse half of the list
        first, sec = head, prev
        while sec:
            next1 = first.next
            next2 = sec.next
            first.next = sec
            sec.next = next1
            first = next1
            sec = next2


        
    

        


        


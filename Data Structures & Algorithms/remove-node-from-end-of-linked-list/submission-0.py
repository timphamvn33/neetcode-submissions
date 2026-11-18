# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse the list and run the loop, find the node at n and point to the next node 

        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        # find the node at n
        node_n = prev
        for _ in range(n-1):
            node_n = node_n.next
        
        # reverse the list to normal list

        prev_1 = None
        curr_1 = prev

        while curr_1:
            nxt = curr_1.next
            if curr_1 != node_n:
                curr_1.next = prev_1
                prev_1 = curr_1

            curr_1 = nxt
        return prev_1


        
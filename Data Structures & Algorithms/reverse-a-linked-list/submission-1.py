# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     1 -> 2 -> 3 -> null
    # null <- curr 

        # iterate solution having o(n) o(1)
        # prev = None
        # curr = head

        # while curr:
        #     next = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next
        # return prev

        #recersive
        if not head or not head.next:
            return head
        result_head = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return result_head
            


        
        
        
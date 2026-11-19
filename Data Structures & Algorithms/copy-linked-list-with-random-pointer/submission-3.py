"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # using the hashmap to store the Node: node.val then
        if not head:
            return None 

        copy_node = {}
        curr = head
        while curr:
            copy_node[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            node_val = copy_node[curr]
            node_val.next = copy_node.get(curr.next)
            node_val.random = copy_node.get(curr.random)
            curr = curr.next
        return copy_node[head]
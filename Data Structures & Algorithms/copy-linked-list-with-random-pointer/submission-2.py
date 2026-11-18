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
        #using the hashmap to store the node value and node address
        copy_node = {}

        if not head:
            return None

        #mp will be head: val
        # iterate thru the Node and add to copy_node. copy_node has only the key head and val not next or random in the values
        curr = head
        while curr:
            copy_node[curr] = Node(curr.val)
            curr = curr.next # curr = val, next, random
        # now we set the next and random for the copy node
        curr = head
        while curr:
            node_copy = copy_node[curr] # node_copy = val, next is None, random is None
            node_copy.next = copy_node.get(curr.next) 
            node_copy.random = copy_node.get(curr.random)
            curr = curr.next
        return copy_node[head]

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
        if not head:
            return None
        d = defaultdict(None)
        def build(head):
            if not head:
                return head
            newnode = Node(head.val)
            newnode.random = head.random
            newnode.next = build(head.next)
            d[head] = newnode
            return newnode
        newhead = Node(head.val)
        newhead.random = head.random
        newhead.next = build(head.next)
        d[head] = newhead
        cur = newhead
        while cur:
            if cur.random:
                cur.random = d[cur.random]
            cur = cur.next
        return newhead
            
            
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return
        def f(head):
            cur = head
            tail = cur
            while cur:
                if cur.child:
                    tmp = cur.next
                    cur.next = cur.child
                    cur.child.prev = cur
                    flttail = f(cur.child)
                    if tmp:
                        tmp.prev = flttail
                    flttail.next = tmp
                    cur.child = None
                    tail = flttail
                    cur = tmp
                else:
                    tail = cur
                    cur = cur.next
            return tail
        f(head)
        return head
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        starthead = head
        def minmax(h):
            #list > 1
            minnode, maxnode = h, h
            minval, maxval = h.val, h.val
            start = h
            while h.next:
                h = h.next
                if h.val >= maxval:
                    maxval = h.val
                    maxnode = h
                if h.val <= minval:
                    minval = h.val
                    minnode = h
                if h is start:
                    break
            return minnode, maxnode
        
        newnode = Node(insertVal)
        if not head:
            node = newnode
            node.next = node
            return node
        elif head.next == head:
            head.next = newnode
            newnode.next = head
            return head
        else:
            minnode, maxnode = minmax(head)
            if insertVal >= maxnode.val or insertVal < minnode.val:
                newnode.next = maxnode.next
                maxnode.next = newnode
                return starthead
            else:
                while head.next:
                    if insertVal >= head.val and insertVal < head.next.val:
                        newnode.next = head.next
                        head.next = newnode
                        return starthead
                    head = head.next

            
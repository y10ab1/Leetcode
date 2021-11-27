# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def add(Q, p1, p2):
            if p1 and p2:
                Q = p1.val + p2.val + Q
                r = Q%10
                q = Q//10
                a = ListNode(val=r)
                a.next = add(q, p1.next, p2.next)
                return a
            elif p1 and not p2:
                Q = p1.val + Q
                r = Q%10
                q = Q//10
                a = ListNode(val=r)
                a.next = add(q, p1.next, None)
                return a
            elif p2 and not p1:
                Q = p2.val + Q
                r = Q%10
                q = Q//10
                a = ListNode(val=r)
                a.next = add(q, None, p2.next)
                return a
            else:
                if Q > 0:
                    a = ListNode(val=Q)
                    return a
                
            
        prehead = ListNode()
        prehead.next = add(0, l1, l2)
        return prehead.next
        
        
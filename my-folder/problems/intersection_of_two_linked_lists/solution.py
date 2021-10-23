# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        Acnt = 0
        Bcnt = 0
        first = True
        A = headA
        B = headB
        while A:
            if A == headB:
                return A
            else:
                A = A.next
        A =headA
        while B:
            if B == headA:
                return B
            else:
                B = B.next
        B =headB
        
        while first or A != headA and B != headB:
            first = False
            if A == B:
                return A
            
            if A :
                A = A.next
            elif Acnt == 0:
                A = headB
                Acnt+=1
            else:
                A = headA
                
            if B :
                B = B.next
            elif Bcnt == 0:
                B = headA
                Bcnt+=1
            else:
                B = headB
            
        return None
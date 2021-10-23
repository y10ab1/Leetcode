# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        Head = ListNode()
        ans = ListNode()
        Head = ans
        while l1 or l2:
            if l1 and l2:
                Q = ((l1.val+l2.val+ans.val)//10)
                R = (l1.val+l2.val+ans.val)%10
                l1, l2 = l1.next, l2.next
                
                nextans = ListNode(Q)
                ans.val = R
                if l1 or l2:
                    ans.next = nextans
                    ans = ans.next
                
            elif not l2:
                Q = ((l1.val+ans.val)//10)
                R = (l1.val+ans.val)%10
                l1 =l1.next
                
                nextans = ListNode(Q)
                ans.val = R
                if l1:
                    ans.next = nextans
                    ans = ans.next
            elif not l1:
                Q = ((l2.val+ans.val)//10)
                R = (l2.val+ans.val)%10
                l2 =l2.next
                
                nextans = ListNode(Q)
                ans.val = R
                if l2:
                    ans.next = nextans
                    ans = ans.next
        if nextans.val !=0:
            ans.next = nextans
            ans = ans.next
        return Head
        
        
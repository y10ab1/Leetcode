# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        s, f = head, head
        
        while f and f.next:
            f = f.next.next
            rev, rev.next, s = s, rev, s.next
        
        if f:
            # odd
            s = s.next
        
        while rev:
            if rev.val != s.val:
                return False
            rev, s = rev.next, s.next
        return True
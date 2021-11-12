# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q = deque([head.val])
        cur = head.next
        if not cur:
            return True
        while cur:
            q.append(cur.val)
            cur = cur.next
        while len(q) > 1:
            if q[0] == q[-1]:
                q.popleft()
                q.pop()
            else:
                return False
        return True
        
            
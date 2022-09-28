# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        cnt = 0
        while cur:
            cur = cur.next
            cnt+=1
        
        if n == cnt:
            return head.next
        
        cur = head
        for i in range(cnt-n):
            if i == cnt-n-1:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
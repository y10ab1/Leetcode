# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = 1
        cur = head
        if head == None or head.next == None:
            return head
        while cur.next:
            size += 1
            cur = cur.next
        
        if k%size == 0:
            return head
        cur.next = head
        for i in range((size-k%size)):
            if i == (size-k)%size-1:
                tail = head
            head = head.next
        tail.next = None            
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd = head
        even = head.next
        evenhead = even
        while odd and even:
            odd.next = even.next
            odd = odd.next
            if odd:
                even.next = odd.next
                even = even.next
        cur = head
        while cur.next:
            cur = cur.next
        cur.next = evenhead
        
        return head
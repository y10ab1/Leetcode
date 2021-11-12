# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        p1 = None
        p2 = head.next
        while p2:
            head.next = p1
            p1 = head
            head = p2
            p2 = head.next
        head.next = p1
        return head
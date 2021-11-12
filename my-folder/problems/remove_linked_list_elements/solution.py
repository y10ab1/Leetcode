# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        pre, cur = None, head
        while cur:
            if cur.val == val and cur != head:
                pre.next = cur.next
                cur = cur.next
            elif cur.val == val and cur == head:
                head = head.next
                pre, cur = None, head
            else:
                pre = cur
                cur = cur.next
        return head
                
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        meet = None
        start = head
        while fast and slow:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                break
            if fast == slow:
                meet = fast
                break
        if not meet:
            return None
        else:
            while meet != start:
                meet = meet.next
                start = start.next
            return start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd, even = head, head.next
        oddtail, evenhead = odd, even

        while odd and even:
            if odd and odd.next:
                odd.next = odd.next.next
                odd = odd.next
                if odd:
                    oddtail = odd

            if even and even.next:
                even.next = even.next.next
                even = even.next

        oddtail.next = evenhead
        return head
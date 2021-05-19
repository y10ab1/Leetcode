# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return head
        Head = head
        Next = head.next
        NewHead = None
        
        while Head:
            Head.next = NewHead
            NewHead = Head
            Head = Next
            if Next:
                Next = Next.next
        return NewHead
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        
        fast, slow, pre = head, head, None
        while not (fast == None or fast.next == None):
            fast = fast.next.next
            pre = slow
            slow = slow.next
            
        pre.next = pre.next.next
            
        
        
        return head
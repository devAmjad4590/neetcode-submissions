# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        curr = head
        before = None

        while curr:
            after = curr.next
            curr.next = before
            before = curr
            curr = after
        head = before
        return head
        

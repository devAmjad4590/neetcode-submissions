# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head and head.next:
            return None
        
        length = 0 
        iterator = head
        while iterator:
            iterator = iterator.next
            length += 1
        
        curr = head
        steps = length - n

        if steps == 0:
            return head.next
        for i in range(steps):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        curr.next = None
        return head

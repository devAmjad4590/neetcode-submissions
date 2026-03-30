# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head and head.next:
            return None
        
        count = head
        length = 0
        while count:
            count = count.next
            length += 1
        
        steps = length - n

        if steps == 0:
            return head.next

        curr = head
        i = 0
        for i in range(steps):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        curr.next = None
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return None

        count = head
        length = 0
        while count:
            count = count.next
            length += 1
        
        i = 0
        steps = length - n
        curr = head
        prev = curr
       
        if steps == 0:
            return head.next

        for i in range(steps):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        curr.next = None
        return head


        
        

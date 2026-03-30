# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        count = head
        while count:
            count = count.next
            length += 1

        step = length - n
        if step == 0:
            return head.next

        dummy = head
        prev = None
        for i in range(step):
            prev = dummy
            dummy = dummy.next
        prev.next = dummy.next
        dummy.next = None
        return head
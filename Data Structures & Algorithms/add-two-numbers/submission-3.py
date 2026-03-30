# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        head = dummy

        while l1 or l2 or carry:
            # this is to deal with the addition between two unequal lengths
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10 # calculate the carry
            val = val % 10 # if number was above 10, then we insert single digits,
            # if there was a carry or not, it will insert a single value and flexible with carries to be calculated
            node = ListNode(val)
            dummy.next = node

            # move the pointers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            dummy = dummy.next
        return head.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode(0)
        head = new_list
        while list1 or list2:
            if not list1 and list2:
                new_list.next = list2
                list2 = list2.next
            elif not list2 and list1:
                new_list.next = list1
                list1 = list1.next
            elif list1.val < list2.val:
                new_list.next = list1
                list1 = list1.next
            else:
                new_list.next = list2
                list2 = list2.next
            new_list = new_list.next
        return head.next
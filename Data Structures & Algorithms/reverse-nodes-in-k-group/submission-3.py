# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
          kthNode = self.getKthNode(groupPrev, k)
          if not kthNode:
            break
          groupNext = kthNode.next
          curr = groupPrev.next
          prev = groupNext
          while curr != groupNext:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
          tmp = groupPrev.next
          groupPrev.next = kthNode
          groupPrev = tmp
          
        return dummy.next

    def getKthNode(self, head, k):
      curr = head
      while curr and k > 0:
        curr = curr.next
        k -= 1
      return curr      
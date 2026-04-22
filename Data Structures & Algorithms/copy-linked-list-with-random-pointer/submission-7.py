"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
          return None
        
        linkedMap = defaultdict(Node)
        dummy = head
        while dummy:
          linkedMap[dummy] = Node(dummy.val)
          dummy = dummy.next
     
        for key, value in linkedMap.items():
          value.next = linkedMap.get(key.next)
          value.random = linkedMap.get(key.random)
        return next(iter(linkedMap.values()))
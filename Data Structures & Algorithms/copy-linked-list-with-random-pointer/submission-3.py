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
        linkMap = defaultdict(Node)

        curr = head
        if not curr:
            return None
        while curr:
            linkMap[curr] = Node(curr.val, None, None)
            curr = curr.next
        
        for key, value in linkMap.items():
            value.next = linkMap.get(key.next)
            value.random = linkMap.get(key.random)
        return next(iter(linkMap.values()))
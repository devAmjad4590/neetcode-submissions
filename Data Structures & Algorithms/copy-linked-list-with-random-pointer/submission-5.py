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
        map = defaultdict(Node)
        curr = head
        if not curr:
                return None
        while curr:
                map[curr] = Node(curr.val, None, None)
                curr = curr.next
        
        for key, val in map.items():
                val.next = map.get(key.next)
                val.random = map.get(key.random)
        return next(iter(map.values()))
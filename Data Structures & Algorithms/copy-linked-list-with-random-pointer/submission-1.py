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
        if head is None:
            return None
        linkMap = defaultdict(Node)
        curr = head
        while curr:
            linkMap[curr] = Node(curr.val, None, None)
            curr = curr.next
        
        for key, value in linkMap.items():
            node = value
            old_node = key
            value.next = linkMap.get(old_node.next)
            value.random = linkMap.get(old_node.random)
        return next(iter(linkMap.values()))


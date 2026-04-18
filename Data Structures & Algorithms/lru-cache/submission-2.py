class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            left = self.left.next
            self.remove(left)
            del self.cache[left.key]

    def insert(self, node):
        prev = self.right.prev
        next = self.right
        prev.next = node
        next.prev = node

        node.next = next
        node.prev = prev

    def remove(self, node):
        prev = node.prev
        after = node.next

        prev.next = after
        after.prev = prev

        node.prev = None
        node.next = None
    
        

class Node:
        def __init__(self, key, val):
                self.val = val
                self.key = key
                self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        prev = self.right.prev
        next = self.right
        prev.next = node
        next.prev = node

        node.next = next
        node.prev = prev

    def remove(self, node):
        prev = node.prev
        next = node.next

        prev.next = node.next
        next.prev = node.prev

        node.next = None
        node.prev = None
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
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key]
        

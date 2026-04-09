class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev, self.next = None, None

class LRUCache:



    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # Left = LRU, Right = MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

        node.next = node.prev = None

    def insert(self, node):
        prev = self.right.prev
        next = self.right
        prev.next = node
        next.prev = node

        node.next = next
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # we remove and insert it so that it is placed to the RIGHT SIDE (MRU)
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value) # its overwriting incase the key alrdy exists, or just adding it if it doesnt. it handles both cases
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

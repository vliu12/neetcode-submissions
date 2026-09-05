class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map key to node

        #store LRU at head, need two dummies left and right before LRU and after MRU
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    # prevNode -> node -> nextNode
        
    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def insert(self, node):
        previous_mru = self.right.prev

        previous_mru.next = node
        node.prev = previous_mru

        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.remove(self.cache[key])
        self.insert(self.cache[key])
        
        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]





        

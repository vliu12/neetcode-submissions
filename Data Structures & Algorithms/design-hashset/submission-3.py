class ListNode:

    def __init__(self, key = None, next = None):
        self.key = key
        self.next = next

class MyHashSet:

    def __init__(self):
        self.map = [ListNode() for i in range(10**4)]
        
    def hash(self, key):
        return key % len(self.map)

    def add(self, key: int) -> None:
        curr = self.map[self.hash(key)]
        while curr.next:
            if curr.next.key == key:
                return
            curr = curr.next
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        curr = self.map[self.hash(key)]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        # do nothing if key does not exist

    def contains(self, key: int) -> bool:
        curr = self.map[self.hash(key)]
        while curr:
            if curr.key == key:
                return True
            curr = curr.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
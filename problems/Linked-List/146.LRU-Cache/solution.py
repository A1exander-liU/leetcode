class LRUNode:
    def __init__(self, val: int):
        self.prev = -1
        self.next = -1
        self.val = val


class LRUCache:

    def __init__(self, capacity: int):
        self.store = {}
        self.capacity = capacity
        self.head = -1
        self.tail = -1

    def _remove_head(self) -> None:
        head = self.head

        if self.store[head].next >= 0:
            self.head = self.store[head].next
            self.store[self.head].prev = -1
        else:
            self.head = -1

        del self.store[head]

    def _add_to_tail(self, key: int, value: int) -> None:
        if len(self.store) == 0:
            self.store[key] = LRUNode(value)
            self.head = key
        else:
            self.store[key] = LRUNode(value)
            self.store[self.tail].next = key
            self.store[key].prev = self.tail

        self.tail = key

    def _move_to_end(self, key: int) -> None:
        if key == self.tail or len(self.store) == 1:
            return

        node = self.store[key]
        head = self.head
        if key == head:
            self.head = self.store[head].next
            self.store[head].prev = -1
        else:
            node = self.store[key]

            prev_key = node.prev
            next_key = node.next

            self.store[prev_key].next = node.next
            self.store[next_key].prev = node.prev

        tail = self.tail
        self.store[tail].next = key
        node.prev = tail
        node.next = -1

        self.tail = key

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1

        self._move_to_end(key)

        return self.store[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store[key].val = value
            self._move_to_end(key)
        elif len(self.store) == self.capacity:
            self._remove_head()
            self._add_to_tail(key, value)
        else:
            self._add_to_tail(key, value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

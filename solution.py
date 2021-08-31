from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.holder = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.holder: return -1
        self.holder.move_to_end(key)
        return self.holder[key]

    def put(self, key: int, value: int) -> None:
        if key in self.holder:
            self.holder[key] = value
        else:
            if self.cap == 0:
                self.holder.popitem(last=False)
                self.holder[key] = value
            else:
                self.holder[key] = value
                self.cap -= 1
        self.holder.move_to_end(key)

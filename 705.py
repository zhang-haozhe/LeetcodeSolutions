class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashList = []

    def add(self, key: int) -> None:
        if key not in self.hashList:
            self.hashList.append(key)

    def remove(self, key: int) -> None:
        if key in self.hashList:
            self.hashList.pop(self.hashList.index(key))

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if(key in self.hashList):
            return True
        return False

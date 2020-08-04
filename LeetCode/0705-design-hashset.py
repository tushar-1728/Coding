class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = dict()
        

    def add(self, key: int) -> None:
        self.d[key] = 1

    def remove(self, key: int) -> None:
        self.d.pop(key, "$")

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.d.keys():
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
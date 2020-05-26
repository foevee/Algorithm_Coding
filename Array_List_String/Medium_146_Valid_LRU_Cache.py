"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

Solution 1 (Lazy way):
Use Python's OrderedDict data structure from collections package.
  It will automatically order the inserted value according to LIFO (last in first out)
  It has a function .popitem(last=True) to return the the newest (last=True) or the oldest (last=False) key-value pair
  So when we want to delete the oldest visit value when out of capacity, we can use .popitem() to remove the oldest one
  Notice, when we use get to visit the key-value existing in the dictionary, we must pop it out then re-insert to make it the newest one 
    (in this way we keep tracking the operation time on each item)

Complexity: O(1) time


Solution 2 (Implement myself, using dictionry and double linkedlist):



Complexity: O(1) time

"""

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.num = 0
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        value = self.cache.pop(key)  #first use normal pop to get the value under the key
        self.cache[key] = value  #then insert again into the dict to make it the newest one (operation)
        return value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            _ = self.cache.pop(key)
            self.cache[key] = value
        else:
            if(self.num>=self.capacity):
                self.cache.popitem(last=False)  #pop out the oldest one
                self.cache[key] = value
            else:
                self.num += 1
                self.cache[key] = value
                


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
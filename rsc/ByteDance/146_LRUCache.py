# coding=utf-8
"""
@Time   : 2020/11/27  17:14 
@Author : Haojun Gao (github.com/VincentGaoHJ)
@Email  : vincentgaohj@gmail.com haojun.gao@u.nus.edu
@Sketch : 
"""


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dict = {}
        self.cache = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.cache.remove(key)
            self.cache.append(key)
        return self.dict.get(key) if self.dict.get(key) else -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        if key not in self.cache:
            if len(self.cache) >= self.capacity:
                pop_key = self.cache.pop(0)
                del self.dict[pop_key]
            self.dict[key] = value
            self.cache.append(key)
        else:
            self.dict[key] = value
            self.cache.remove(key)
            self.cache.append(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
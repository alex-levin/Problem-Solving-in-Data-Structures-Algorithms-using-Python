#!/usr/bin/env python
class HashTableSC(object):
    def __init__(self):
        self.table_size = 512
        self.adj_list = [[] for _ in range(self.table_size)]

    def compute_hash(self, key):
        #  division method
        hash_value = key
        return hash_value % self.table_size

    def resolver_fun(self, i):
        return i

    def resolver_fun2(self, i):
        return i * i

    def add(self, value):
        index = self.compute_hash(value)
        self.adj_list[index].append(value)

    def remove(self, value):
        index = self.compute_hash(value)
        if value in self.adj_list[index]:
            self.adj_list[index].remove(value)
            return True
        return False

    def print(self):
        for i in range(self.table_size):
            if len(self.adj_list[i]) != 0:
                print("Value at index ::" , i , "are :: ", end="")
                for value in self.adj_list[i]:
                    print(value, end=' ')
                print("")

    def find(self, value):
        index = self.compute_hash(value)
        if value in self.adj_list[index]:
            return True
        return False

ht = HashTableSC()
ht.add(1)
ht.add(2)
ht.add(3)
ht.print()

print("find 2 :", ht.find(2))

ht.remove(2)
print("After deleting node with key 2.")
print("find 2 :", ht.find(2))

"""
Value at index :: 1 are :: 1 
Value at index :: 2 are :: 2 
Value at index :: 3 are :: 3 
find 2 : True
After deleting node with key 2.
find 2 : False
"""
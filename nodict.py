#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'sohailadev'


class Node:
    def __init__(self, key, value=None):
        self.hash = hash(key)
        self.key = key
        self.value = value

    def __repr__(self):
        # Your code here
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        # Your code here
        return self.key == other.key


class NoDict:
    def __init__(self, num_buckets=10):
        """initializaion of object"""
        self.num_buckets = num_buckets
        self.buckets = [[] for _ in range(self.num_buckets)]

    def __repr__(self):
        """Return a string representing the NoDict contents."""
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}' for i, bucket in enumerate(self.buckets)])

    def add(self, key, value):
        """add new node in buckets."""
        new_node = Node(key, value)
        key_hash = new_node.hash % self.num_buckets
        key_exists_flag = False
        for index, bucket in enumerate(self.buckets):
            if len(bucket) > 0:
                k = bucket[0].key
                v = bucket[0].value
                if k == new_node.key:
                    key_exists_flag = True
                    break
        if key_exists_flag:
            self.buckets[key_hash][0].value = new_node.value
        else:
            self.buckets[key_hash].append(new_node)

    def get(self, key):
        """retun node on given key else raise error"""
        node_to_find = Node(key)
        key_hash = node_to_find.hash % self.num_buckets
        if len(self.buckets[key_hash]) > 0:
            for bucket in self.buckets[key_hash]:
                if bucket.key == key:
                    return bucket.value
                else:
                    raise KeyError(f'{key} not found')
        else:
            raise KeyError(f'{key} not found')

    def __getitem__(self, key):
        """override the dunder getitem metod"""
        node_to_find = Node(key)
        key_hash = node_to_find.hash % self.num_buckets
        for bucket in self.buckets[key_hash]:
            if bucket.key == key:
                return bucket.value
            else:
                raise KeyError(f'{key} not found')

    def __setitem__(self, key, value):
        """override the setitem """
        new_node = Node(key, value)
        key_hash = new_node.hash % self.num_buckets
        key_exists_flag = False
        for index, bucket in enumerate(self.buckets):
            if len(bucket) > 0:
                k, v = bucket
                if k == new_node.key:
                    key_exists_flag = True
                    break
        if key_exists_flag:
            self.buckets[key_hash][index] = new_node
        else:
            self.buckets[key_hash].append(new_node)

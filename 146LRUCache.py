# 146. LRU Cache
# Medium
# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
#
# The cache is initialized with a positive capacity.
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
# LRUCache cache = new LRUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4

from collections import OrderedDict


# Solution I: OrderedDict
#
# Solution II: dict + doubleLinkedList

# Time Complexity O(1)
# Space Complexixty O(capacity)

class ListNode():
    def __init__(self, key, value, pre=None, next=None):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache():

    #     1   2
    #     1   2
    #
    #         2|   1   3
    #         2|   1   3
    #
    #             1|   3   4
    #             1|   3   4
    #
    #                     4   3
    #                     4   3
    #
    #                         3   4
    #                         3   4
    #
    #         cache_dict = {}
    #                                                Most recently Used - Add new node here
    #         cache_key = key 1   cache_value = Node (key 1 -> value 1)  head
    #                                             ^
    #                                             |
    #                                             V
    #         cache_key = key 1   cache_value = Node (key 1 -> value 1)                         #                                             ^
    #                                             |
    #                                             V   Least recently Used - Remove node here
    #        cache_key = key 1   cache_value = Node (key 1 -> value 1)  tail
    #
    #        1. move to head:
    #             1 -> 2 -> 3 -> 4
    #           head       node tail
    #           (1) remove node
    #           (2) add node to head
    #
    #         (1) remove node:
    #             1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
    #           head      pre_n node next_n    tail
    #             pre_n.next =  next_n
    #             next_n.pre = pre_n
    #
    #         (2) add node to head
    #           head ------> 1 -> 2 -> 3 -> 4
    #                 node  next_n
    #
    #         head.next = node
    #         node.pre = head
    #         node.next = next_n
    #         next_n.pre = node
    #
    #         2. Remove from tail:
    #             1 -> 2 -> 3 -> 4 <----------> tail
    #            head      pre_n node
    #            pre_n.next = tail
    #            tail.pre = pre_n

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.cache_dict = {}

        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node_to_head(self, node):

        next_n = self.head.next

        self.head.next = node
        node.pre = self.head
        node.next = next_n
        next_n.pre = node

    def remove_node(self, node):

        pre_n = node.pre
        next_n = node.next

        pre_n.next = next_n
        next_n.pre = pre_n

    def remove_from_tail(self):

        node = self.tail.pre
        pre_n = node.pre

        pre_n.next = self.tail
        self.tail.pre = pre_n

        return node

    def move_to_head(self, node):

        self.remove_node(node)
        self.add_node_to_head(node)

    def get_size(self):

        return len(self.cache_dict)

    def get(self, key: int) -> int:
        # if exist, move the node to the head

        if key not in self.cache_dict:
            return -1

        node = self.cache_dict[key]
        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        # add the node to the head

        if key in self.cache_dict:
            node = self.cache_dict[key]
            node.value = value
            self.move_to_head(node)
        else:
            node = ListNode(key, value)
            self.cache_dict[key] = node
            self.add_node_to_head(node)

        if self.get_size() > self.capacity:
            tail_node = self.remove_from_tail()
            del self.cache_dict[tail_node.key]

    def p(self):

        print(self.cache_dict.keys())
        node = self.head
        while node:
            print(f' cache_dict = {node.key} :  (Node = {node.key} {node.value}), ')
            node = node.next

        print('----')
        node = self.tail
        while node:
            print(f' cache_dict = {node.key} :  (Node = {node.key} {node.value}), ')
            node = node.pre
        print('---------------------------------')


'''
class LRUCache(OrderedDict):
    def __init__(self, capacity: int):

        self.capacity = capacity


    def get(self, key: int) -> int:

        if key not in self:
            return -1

        self.move_to_end(key)
        return self[key]


    def put(self, key: int, value: int) -> None:

        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False)
'''

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
'''
460. LFU Cache
Hard

Design and implement a data structure for Least Frequently Used (LFU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists
in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reaches its capacity, it should invalidate the least frequently
used item before inserting a new item. For the purpose of this problem, when
there is a tie (i.e., two or more keys that have the same frequency), the least
recently used key would be evicted.

Note that the number of times an item is used is the number of calls to the get
and put functions for that item since it was inserted. This number is set to zero
when the item is removed.



Follow up:
Could you do both operations in O(1) time complexity?



Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''


# capacity = 2         most recent <----------> least recent
#                      most frequent <----------> least frequent
# cache.put(1, 1);
#             1
#             1
# frequency:  1
# cache.put(2, 2);
#             2   1
#             2   1
# frequence:  1   1
# cache.get(1);       // returns 1
#             1   2
#             1   2
# frequence:  2   1
# cache.put(3, 3);    // evicts key 2
#             1   3
#             1   3
# frequence:  2   1
# cache.get(2);       // returns -1 (not found)
#             not found
# cache.get(3);       // returns 3.
#             3   1
#             3   1
# frequence:  2   2
# cache.put(4, 4);    // evicts key 1.
#             3   4
#             3   4
# frequence:  2   1
# cache.get(1);       // returns -1 (not found)
#             not found
# cache.get(3);       // returns 3
#             3   4
#             3   4
# frequence:  3   1
# cache.get(4);       // returns 4
#             3   4
#             3   4
# frequence:  3   2
#
# Solution I: using 1 dictionary, not O(1) time complexity
#
#                                            head
#                                             ^
#         cache_dict = {}                     |
#                                             V
#                                                Most recently ised
#                                                Most frequently used
#                                                * add node from here, and move to the correct position according to the frequency
#         cache_key = key 1   cache_value = Node (key 1 -> value 1)
#                                             ^
#                                             |
#                                             V
#         cache_key = key 2   cache_value = Node (key 2 -> value 2)
#                                             ^
#                                             |
#                                             V   Least recently used
#                                                 Least frequently used
#                                                 * remove node from here
#         cache_key = key 3   cache_value = Node (key 3 -> value 3)
#                                             ^
#                                             |
#                                             V
#                                            tail
#
# Solution II: use 2 dictionary
#
#     frequency N
#
#         head <---> Node <---> Node <---> Node <---> tail
#                     |          |           |
#                    key 1      key 2      key 3
#                  value 1     value 2    value 3
#                   fre N       fre N       fre N
#
#     frequency N-1
#        ...
#     frequency 1

# Time O(1), Space O(), runtime = 320 ms
class ListNode():

    def __init__(self, key, value, fre=None, pre=None, next=None):
        self.key = key
        self.value = value
        self.fre = fre
        self.pre = pre
        self.next = next


class DLinkedList():

    def __init__(self):
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.next = self.tail
        self.tail.pre = self.head

    def remove_node(self, node):
        pre_n = node.pre
        next_n = node.next

        pre_n.next = next_n
        next_n.pre = pre_n

    def add_to_head(self, node):
        next_n = self.head.next

        self.head.next = node
        node.pre = self.head
        node.next = next_n
        next_n.pre = node

    def remove_from_tail(self):
        node = self.tail.pre
        pre_n = node.pre

        pre_n.next = self.tail
        self.tail.pre = pre_n

        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_node = {}
        self.fre_dll = {}
        self.size = 0
        self.min_fre = 1

    def remove(self, dll, fre):
        if dll.head.next == dll.tail:
            if self.min_fre == fre:
                self.min_fre = fre + 1
            if fre != 1:
                del self.fre_dll[fre]
        else:
            self.fre_dll[fre] = dll

    def remove_from_dll(self, node):
        fre = node.fre
        dll = self.fre_dll[fre]
        dll.remove_node(node)

        self.remove(dll, fre)

    def remove_from_dll_tail(self, dll, fre):
        dll.remove_from_tail()

        self.remove(dll, fre)

    def add_to_dll(self, node):
        fre = node.fre
        dll = self.fre_dll.get(fre, DLinkedList())
        dll.add_to_head(node)
        self.fre_dll[fre] = dll

    def get(self, key: int) -> int:
        if key not in self.key_node:
            return -1

        node = self.key_node[key]
        self.remove_from_dll(node)

        node.fre += node.fre
        self.add_to_dll(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.key_node:
            node = self.key_node[key]
            node.value = value

            self.remove_from_dll(node)

            node.fre += 1
            self.add_to_dll(node)

        else:
            fre = 1
            node = ListNode(key, value, fre)
            self.key_node[key] = node

            self.add_to_dll(node)

            self.size += 1
            if self.size > self.capacity:
                min_dll = self.fre_dll[self.min_fre]

                last_node = min_dll.tail.pre
                self.remove_from_dll_tail(min_dll, self.min_fre)

                del self.key_node[last_node.key]
                self.size -= 1

            self.min_fre = 1

    def p(self):
        print(self.key_node.keys())
        for k, v in self.key_node.items():
            print(f'key = {k} (Node key={v.key} val={v.value} fre={v.fre})')
        print(f'min_fre = {self.min_fre}')
        for k, v in self.fre_dll.items():
            print(f'fre = {k}')
            node = v.head
            while node:
                print(f' fre = {k}  (Node key={node.key} val={node.value} fre={node.fre})')
                node = node.next
        print('---------------------------------------')

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
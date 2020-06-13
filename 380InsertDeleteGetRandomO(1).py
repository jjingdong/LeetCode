'''
380. Insert Delete GetRandom O(1)
Medium

Design a data structure that supports all following operations in average O(1) time.

	1.	insert(val): Inserts an item val to the set if not already present.
	2.	remove(val): Removes an item val from the set if present.
	3.	getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

Example:
// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();

'''


class RandomizedSet:

    # dict:
    # insert O(1)
    # remove O(1)
    # getRandom ??
    #
    # list:
    # insert O(1)
    # remove O(N)
    # getRandom O(1)
    #
    # Solution: Dict + List

    # Time O(1), Space O(N), runtime = 100 ms
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # {val:index}
        self.rs_dict = {}
        self.lst = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.rs_dict:
            return False
        self.rs_dict[val] = len(self.lst)
        self.lst.append(val)

        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.rs_dict:
            return False
        index = self.rs_dict[val]
        last_value = self.lst[-1]
        self.lst[index], self.lst[-1] = self.lst[-1], self.lst[index]
        self.lst.pop(-1)

        self.rs_dict[val], self.rs_dict[last_value] = self.rs_dict[last_value], self.rs_dict[val]
        self.rs_dict.pop(val)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        index = int(random.random() * len(self.lst))
        value = self.lst[index]
        return value

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
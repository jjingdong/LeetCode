'''
904. Fruit Into Baskets
Medium

In a row of trees, the i-th tree produces fruit with type tree[i].
You start at any tree of your choice, then repeatedly perform the following steps:
	1.	Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
	2.	Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.
You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.
What is the total amount of fruit you can collect with this procedure?
 
Example 1:
Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
Example 2:
Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].
Example 3:
Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].
Example 4:
Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.

'''


class Solution:

    # Question: What is the length of longest subarray that contains up to two distinct integers?

    # Time O(N) Space O(N)
    def totalFruit(self, tree: List[int]) -> int:

        i, j, count = 0, 0, 0
        types = collections.defaultdict(int)

        for j in range(len(tree)):
            cur = tree[j]
            types[cur] += 1

            while len(types) == 3:
                cur_i = tree[i]
                types[cur_i] -= 1
                i += 1

                if types[cur_i] == 0:
                    types.pop(cur_i)

            count = max(count, j - i + 1)

        return count



'''
365. Water and Jug Problem
Medium

263

692

Add to List

Share
You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True
Example 2:

Input: x = 2, y = 6, z = 5
Output: False
'''


class Solution:

    # Solution I: Math
    #
    # Check if z is a multiple of GCD(x,y)
    # GCD = greatest common divisor
    #
    # Solution II: BFS
    #
    # Note. need to read this: https://leetcode.com/problems/water-and-jug-problem/discuss/83709/Breadth-First-Search-with-explanation.

    # Time O() Space O()
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        # from fractions import gcd
        return z == 0 or x + y >= z and z % gcd(x, y) == 0

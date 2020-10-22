'''
735. Asteroid Collision
Medium

We are given an array asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
Example 1: 
Input:
asteroids = [5, 10, -5]
Output: [5, 10]
Explanation:
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.

Example 2: 
Input:
asteroids = [8, -8]
Output: []
Explanation:
The 8 and -8 collide exploding each other.

Example 3: 
Input:
asteroids = [10, 2, -5]
Output: [10]
Explanation:
The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.

Example 4: 
Input:
asteroids = [-2, -1, 1, 2]
Output: [-2, -1, 1, 2]
Explanation:
The -2 and -1 are moving left, while the 1 and 2 are moving right.
Asteroids moving the same direction never meet, so no asteroids will meet each other.
'''


class Solution:

    # Solution I: Use Stack
    # all the collisions must occur right to left
    # a row of asteroids is table if no further collisions
    # Note. This is not done,

    #         [5, 10, -5]
    #
    #     eg.
    #         5   10  -5
    #         --> --> <--
    #         result = [5, 10]
    #
    #     eg.
    #         8       -8
    #         -->    <--
    #         result = []
    #
    #     eg.
    #         10    2   -5
    #         -->  -->  <--
    #         10   -5
    #         -->  <--
    #         result = [10]
    #
    #     eg.
    #         -2      -1      1       2
    #         <--    <--     -->     -->
    #         result = [-2, -1, 1, 2]
    #
    #     using stack

    # Time O(N) Space O(N)
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        if not asteroids: return None

        stack = collections.deque([])
        for a in asteroids:

            stack.append(a)
            while len(stack) >= 2 and stack[-1] < 0 < stack[-2]:
                top = stack.pop()
                second_top = stack.pop()
                if second_top < -top:
                    stack.append(top)
                elif second_top > -top:
                    stack.append(second_top)

        return stack


'''
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        if asteroids is None: return None
        if asteroids == [] : return []

        i = 0
        result = [asteroids[0]]
        skipJ = False

        for j in range(1, len(asteroids)):

            if skipJ == False:


                if asteroids[i] > 0 and asteroids[j] < 0:
                    if asteroids[i] == - asteroids[j]:
                        i += 2
                        skipJ = True


                    else:
                        value = asteroids[i] + asteroids[j]
                        result.append(value)
                        i += 2
                        skipJ = True

                else:
                    result.append(asteroids[j])
                    i += 1

            return result
'''


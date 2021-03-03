'''
301. Remove Invalid Parentheses
Hard

Remove the minimum number of invalid parentheses in order to make the input string
valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
'''


class Solution:

    #         (   )   (   )   )   (   )
    #         1   0   1   0   -1
    #                         |invalid

    #             (   )   (   )   )   (   )
    #                             |
    #                             remove

    #             (   )   (   )   )   (   )
    #                         |
    #                         remove

    # each time, delete 1 char, and see if this is a valid string
    # ()()))()
    # (()))()
    # ()()))(
    # ()())()

    # each time, also check if right, or left, or both needed to be deleted

    def removeInvalidParentheses(self, s: str) -> List[str]:

        # check if the string is valid
        def is_valid(s):

            count = 0
            for char in s:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False

            return count == 0

        # count which bracket to remove
        def count_lr(s):
            count_l = 0
            count_r = 0
            for char in s:
                if char == '(':
                    count_l += 1
                elif char == ')':
                    count_r += 1
            return count_l, count_r

        str_set = set()
        str_set.add(s)
        while True:

            result = []
            for one_str in str_set:
                if is_valid(one_str):
                    result.append(one_str)
            if result:
                return result

            new_str_set = set()
            for one_str in str_set:

                no_l, no_r = count_lr(one_str)
                diff = no_l - no_r
                for i in range(len(one_str)):

                    char = one_str[i]
                    if (char == '(' and diff > 0) \
                            or (char == ')' and diff < 0) \
                            or diff == 0:
                        new_str = one_str[:i] + one_str[i + 1:]
                        new_str_set.add(new_str)
            str_set = new_str_set

        return None


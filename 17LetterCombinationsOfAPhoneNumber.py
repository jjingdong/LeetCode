'''
17. Letter Combinations of a Phone Number
Medium

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.

'''


class Solution:

    # Solution I: Backtracking, recursion
    #
    # Solution II: Iteration ----> don't know how to do it, for now

    #     # Time O() Space O()
    #     def letterCombinations(self, digits: str) -> List[str]:

    #         if not digits: return []

    #         results = []
    #         l_dict = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl',
    #                        '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

    #         for d in digits:
    #             for v in l_dict[d]:
    #                 for i in range(len(results)):
    #                     result[i] = result[i] + r

    #         return results

    # Time O(3^N) Space O(3^N), runtime = 28 ms
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits: return []

        results = []
        l_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                  '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        def combine(index, build):

            if len(build) == len(digits):
                results.append(build)
                return

            d = digits[index]
            for v in l_dict[d]:
                combine(index + 1, build + v)

        combine(0, '')
        return results



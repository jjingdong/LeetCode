'''
22. Generate Parentheses
Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''


class Solution:

    # Time O(4^N / square(N)) Space O(4^N / square(N))
    def generateParenthesis(self, n: int) -> List[str]:

        def generate(build, count_l, count_r):
            if len(build) == 2 * n:
                results.append(build)
                return

            if count_l < n:
                generate(build + '(', count_l + 1, count_r)
            if count_l > count_r:
                generate(build + ')', count_l, count_r + 1)

        results = []
        generate('', 0, 0)
        return results


'''
    # Time O(4^N * N) Space O(4*N * N)
    def generateParenthesis(self, n: int) -> List[str]:

        # Time O(N) Space O(1)
        def is_parentheses(string):
            count = 0
            for s in string:
                if s == '(': 
                    count += 1
                else:
                    count -=1
                if count < 0:
                    return False  
            return count == 0

        # Time O(4^N) Space O(4^N)
        def generate(build): 
            if len(build) == n * 2:
                if is_parentheses(build):
                    results.append(build)
                return

            generate(build + '(')
            generate(build + ')')

        if not n: return ['']       
        results = []
        generate('')
        return results 
'''
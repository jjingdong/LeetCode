class Solution:

    # S = "a1b2"
    # a1b
    # a1B
    # A1b
    # A1B

    # Time O(2^N * N)
    # Space O(2^N * N)
    def letterCasePermutation(self, S: str) -> List[str]:

        if S is None: return None
        if S == '': return ''

        results = []

        def mutation(substr, index):

            if index == len(S):
                results.append(substr)
            else:
                cur = S[index]
                if cur.isalpha():
                    substr1 = substr + cur.lower()
                    mutation(substr1, index + 1)
                    substr2 = substr + cur.upper()
                    mutation(substr2, index + 1)
                else:
                    mutation(substr + cur, index + 1)

        mutation("", 0)
        return results




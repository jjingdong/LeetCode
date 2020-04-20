# 202. Happy Number
# Easy
#
# Write an algorithm to determine if a number is "happy".
# A happy number is a number defined by the following process: Starting with any positive integer,
# replace the number by the sum of the squares of its digits, and repeat the process until the
# number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include
# 1. Those numbers for which this process ends in 1 are happy numbers.
# Example: 
# Input: 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

class Solution:

    # Time O(logN) Space O(1)
    def isHappy(self, n: int) -> bool:

        cycles = {4, 16, 37, 58, 89, 145, 42, 20}

        def getSum(n):

            sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                sum += digit ** 2
            return sum

        while n != 1 and n not in cycles:
            n = getSum(n)

        return n == 1

    '''
    # Time O(logN) Space O(1)
    def isHappy(self, n: int) -> bool:

        def getSum(n):

            sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                sum += digit ** 2
            return sum 

        s = n
        f = getSum(n)
        while f != 1 and s != f:
            s = getSum(n)
            f = getSum(getSum(f))

        return f == 1

    '''

    '''
    def isHappy(self, n: int) -> bool:

        def getSum(n):

            sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                sum += digit ** 2
            return sum 

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = getSum(n)

        return n == 1
    '''
    # Time O(logN) Space O(logN)

    '''
    # Time O(logN) Space O(logN)
    def isHappy(self, n: int) -> bool:

        def getSum(n):

            digits = []
            def getDigits(n):

                if n < 10 and n > 0:
                    digits.append(n)
                elif n >= 10:
                    getDigits(n % 10)
                    getDigits(n // 10)

            getDigits(n)
            sum = 0
            for d in digits:
                sum += d * d

            return sum

        seen = set()
        sum = getSum(n)
        if sum == 1:
            return True
        while sum != 1 and sum not in seen:
            seen.add(sum)
            sum = getSum(sum)

        if sum == 1:
            return True
        else:
            return False
    '''


# 412. Fizz Buzz
# Easy
#
# Write a program that outputs the string representation of numbers from 1 to n.
#
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
#
# Example:
#
# n = 15,
#
# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]
class Solution:

    # 3 -> Fizz
    # 5 -> Buzz
    # 3 and 5 -> FizzBuzz

    # Time O(N) Space O(1), runtime = 44 ms
    def fizzBuzz(self, n: int) -> List[str]:
        if not n: return None

        THREE = 'Fizz'
        FIVE = 'Buzz'

        return [THREE * (not i % 3) + FIVE * (not i % 5) or str(i) for i in range(1, n + 1)]


'''
    # Time O(N) Space O(1), runtime = 44 ms
    def fizzBuzz(self, n: int) -> List[str]:

        if not n: return None

        three = 'Fizz'
        five = 'Buzz'

        results = []
        for num in range(1, n+1):

            r = ''
            if num % 3 == 0:
                r += three
            if num % 5 == 0:
                r += five
            if r == '':
                r = str(num)
            results.append(r) 
        return results
'''

'''
    #Time O(n)
    #Space O(1)
    def fizzBuzz(self, n: int) -> List[str]:

        results = []
        for i in range(1, n+1):

            if i % 3 == 0 and i % 5 == 0:
                results.append("FizzBuzz")
            elif i % 3 == 0:
                results.append("Fizz")
            elif i % 5 == 0:
                results.append("Buzz")
            else:
                results.append(str(i))

        return results
'''


'''
A string is called balanced when every letter occurring in the string, appears both in upper and lowercase.
For example, the string "CATattac" is balanced ('a','c' and 't' occur in both cases), but
'Madam' is not ('d' and 'a' appear only in lowercase). Note that the number of occurrences does not matter.
Write a function:
function myFunc(string);
that, given a string, of length N, returns the length of the shortest balanced fragment of string.
If string does not contain any balanced fragments, the function should return -1.
Ex)
1. Given string = "azABaabza", the function should return 5. The shortest balanced fragment string is "ABaab"
2. Given string = "TacoCat", the function should return -1. There is no balanced fragment.
3. Given string = "AcZCbaBz", the function should return 8. The shortest balanced fragment is the whole string.
4. Given string = "abc", the function should return -1.
Assume that:
- N is an integer within the range [1..200]
- string consists only of letters ('a'-'z' and/or 'A'-'Z')
In your solution, focus on correctness, not performance.
'''

# Solution I
import collections


def balanced(input):
    def helper(l, r):

        substr = input[l:r + 1]
        a_set = set(substr)
        if len(a_set) % 2 != 0:
            return False

        for item in a_set:
            if not (item.isupper() and item.lower() in a_set) and not (item.islower() and item.upper() in a_set):
                return False

        print(a_set)

        return True

    size = len(input)
    window_size = 2
    for s in range(window_size, size):
        for i in range(size):
            if helper(i, i + s):
                return s + 1

    return -1

# Testing
input_1 = 'azABaabza'
expected_output_1 = 5
print(output_1)
print(output_1 == expected_output_1)

input_2 = 'TacoCat'
output_2 = balanced(input_2)
expected_output_2 = -1
print(output_2)
print(output_2 == expected_output_2)

input_3 = 'AcZCbaBz'
output_3 = balanced(input_3)
expected_output_3 = 8
print(output_3)
print(output_3 == expected_output_3)

input_4 = 'abc'
output_4 = balanced(input_4)
expected_output_4 = -1
print(output_4)
print(output_4 == expected_output_4)
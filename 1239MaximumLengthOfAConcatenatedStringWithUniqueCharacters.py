'''
1239. Maximum Length of a Concatenated String with Unique Characters
Medium

Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.



Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26


Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.
'''



# This is not a solution
# It's recursion approach for getting all combination, without set checking
# result = ['', 'un', 'iq', 'uniq', 'ue', 'unue', 'ique', 'unique']
def maxLength(self, arr: List[str]) -> int:
    result = []

    def helper(build, index):
        if index == -1:
            result.append(build)
            return 0

        helper(arr[index] + build, index - 1)
        helper(build, index - 1)

    size = len(arr)
    helper('', size - 1)
    print(result)
    return 0

# This is not a solution
# It's recursion approach for getting all combination, without set checking
# result = ['', 'un', 'iq', 'uniq', 'ue', 'unue', 'ique', 'unique']
def maxLength(self, arr: List[str]) -> int:

    result = []

    def helper(build, index):
        result.append(build)

        for i in range(index + 1):
            helper(arr[i] + build, i - 1)

    size = len(arr)
    helper('', size - 1)
    print(result)
    return 0

# recursion, take or not take strategy
def maxLength(self, arr: List[str]) -> int:

    def helper(build, index):

        if index == size:
            return len(build)

        new_build = build + arr[index]
        a = helper(build, index + 1)

        b = float('-inf')
        # no overlapping
        if len(set(new_build)) == len(build + arr[index]):
            b = helper(build + arr[index], index + 1)

        return max(a, b)

    size = len(arr)
    return helper('', 0)


# recursion, top down
def maxLength(self, arr: List[str]) -> int:

    # if the input has an item, which has duplicated chars
    new_arr = []
    for item in arr:
        if len(set(item)) == len(item):
            new_arr.append(item)
    arr = new_arr

    def helper(build, index):
        if index == -1:
            return len(build)

        # overlapping:
        if set(build) & set(arr[index]):
            return helper(build, index - 1)
        else:
            # take or not take
            a = helper(build, index - 1)
            b = helper(arr[index] + build, index - 1)
            return max(a, b)

    size = len(arr)
    return helper('', size - 1)


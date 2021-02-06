'''
Given a string s and an int k, return all unique substrings of s of size k with k distinct characters.

Example 1:

Input: s = "abcabc", k = 3
Output: ["abc", "bca", "cab"]
Example 2:

Input: s = "abacab", k = 3
Output: ["bac", "cab"]
Example 3:

Input: s = "awaglknagawunagwkwagl", k = 4
Output: ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag",
        "nagw", "agwk", "kwag"]
Explanation:
Substrings in order are: "wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun",
        "wuna", "unag", "nagw", "agwk", "kwag", "wagl"
"wagl" is repeated twice, but is included in the output once.
Constraints:

The input string consists of only lowercase English letters [a-z]
0 ≤ k ≤ 26
Solution
'''

'''
Diagram

  a b c a b c           k = 3
  -----
    -----
      -----

  a b a c a b           k = 3
    -----
        -----

  a w a g l k n a g a w u n a g w k w a g l           k = 4
    -------
      -------
        -------
          -------
            -------
              -------
                -------


Solution I. Brute Force

result = []
iterate stirng s
    find substring, which length is k = 4
    if the substring has unique chars:
      if the result
      add it to the final result array


Solution II. sliding window      

index = 0     3
        a w a g l k n a g a w u n a g w k w a g l
        |   |
        i   j                            {a:1}
        |     |
        i     j                       {a:2, w:1, g:1}
          |     |
          i     j      move both i,j  {a:1, w:1, g:1, l:1}

    when to move?   1. size is bigger than 4
                    2. count is bigger than 1

List of sliding window problem:
https://leetcode.com/tag/sliding-window/  

Brainstorm:

dictionary
set
array

'''
# # Time O() Space O()
# def find_substring(s, k):

#     if not s or not k: return []
#     results = []
#     c_set = set()
#     size = k

#     i = 0
#     for j in range(len(s)):
#         while s[j] in c_set:
#             c_set.remove(s[i])
#             i += 1

#         c_set.add(s[j])

#         if len(c_set) == k:
#             if s[i: j+1] not in results:
#                 results.append(s[i: j+1])
#                 c_set.remove(s[i])
#                 i += 1

#     return results


# # Time O() Space O()
# def find_substring(s, k):

#     if not s or not k: return []
#     results = []
#     c_set = set()
#     size = k

#     i = 0
#     for j in range(len(s)):
#         c_set.add(s[j])

#         while s[j] in c_set:
#             c_set.remove(s[i])
#             i += 1

#         if len(c_set) == k:
#             if s[i: j+1] not in results:
#                 results.append(s[i: j+1])
#                 c_set.remove(s[i])
#                 i += 1

#     return results

# Brute Force
import collections


def find_substring(s, k):
    result = []
    for i in range(len(s)):
        subs = s[i:i + k]
        if len(set(subs)) == k and subs not in result:
            result.append(subs)
    return result


'''
Testing
'''

s = "abcabc"
k = 3
expected_result = ["abc", "bca", "cab"]
output = find_substring(s, k)
print(f'output = {output}')
print(expected_result == output)

s = "abacab"
k = 3
expected_result = ["bac", "cab"]
output = find_substring(s, k)
print(f'output = {output}')
print(expected_result == output)

s = "awaglknagawunagwkwagl"
k = 4
expected_result = ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
output = find_substring(s, k)
print(f'output = {output}')
print(expected_result == output)











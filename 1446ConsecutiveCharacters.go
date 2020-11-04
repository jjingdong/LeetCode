/*
1446. Consecutive Characters
Easy

Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.



Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
Example 3:

Input: s = "triplepillooooow"
Output: 5
Example 4:

Input: s = "hooraaaaaaaaaaay"
Output: 11
Example 5:

Input: s = "tourist"
Output: 1


Constraints:

1 <= s.length <= 500
s contains only lowercase English letters.
*/

// Time O(N) Space O(1)
// Go runtime is always 100%
func maxPower(s string) int {

    max_count := 1
    count := 1

    for i := 0; i < len(s)-1; i++ {

        if s[i] == s[i+1] {
            count ++
        } else {
            count = 1
        }

        if max_count < count{
            max_count = count
        }

    }
    return max_count
}
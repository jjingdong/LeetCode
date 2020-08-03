'''
125. Valid Palindrome
Easy

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''

class Solution:

    # Note. \w is same as [a-zA-Z0-9_]

    # Time O(N) Space O(1) runtime = 120 ms
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        pattern = '[a-zA-Z0-9]'
        s = ''.join(c for c in s if re.fullmatch(pattern, c))
        return s == s[::-1]


'''
    # Time O(N) Space O(N), runtime = 40 ms
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        s = ''.join(c for c in s if c.isalnum())     
        return s == s[::-1]
'''

'''
    # Time O(N) Space O(1), runtime = 180 ms
    def isPalindrome(self, s: str) -> bool:

        i,j = 0, len(s)-1
        pattern = '[a-zA-Z0-9]'
        while i <= j:

            if re.fullmatch(pattern, s[i]) and re.fullmatch(pattern, s[j]):
                if s[i].lower() != s[j].lower():
                    return False
                else:
                    i += 1
                    j -= 1
            elif not re.fullmatch(pattern, s[i]):
                i += 1
            elif not re.fullmatch(pattern, s[j]):
                j -= 1   

        return True
'''

'''
    # Time O(N) Space O(1), runtime = 52 ms
    def isPalindrome(self, s: str) -> bool:

        if not s: return True

        i, j = 0, len(s) - 1
        while i <= j:

            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() != s[j].lower():
                    return False
                else:
                    i += 1
                    j -= 1
            elif not s[i].isalnum():
                i +=1
            elif not s[j].isalnum():
                j -= 1

        return True
'''

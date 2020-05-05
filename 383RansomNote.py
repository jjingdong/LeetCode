'''
383. Ransom Note
Easy

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
Each letter in the magazine string can only be used once in your ransom note.
Note: You may assume that both strings contain only lowercase letters.
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''


class Solution:

    # Time O(K) Space O(1)
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if ransomNote is None or magazine is None: return None
        if len(ransomNote) > len(magazine): return False

        magazine_count = collections.Counter(magazine)

        for c in ransomNote:
            if c in magazine_count:
                if magazine_count[c] >= 1:
                    magazine_count[c] -= 1
                else:
                    return False
            else:
                return False

        return True


'''
    # Time O(NK) Space O(K)
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if ransomNote is None or magazine is None: return None

        for c in ransomNote:
            if c not in magazine:
                return False
            else:
                index = magazine.index(c)
                magazine = magazine[:index] + magazine[index+1:]

        return True
'''

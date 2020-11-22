from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = defaultdict(int)
        for ch in magazine:
            magazine_count[ch] += 1
        for ch in ransomNote:
            if magazine_count[ch] == 0:
                return False
            magazine_count[ch] -= 1
        return True


# without using hashmap:
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran = list()
        # but since strings are immutable, therefore this is faster but in terms of storage this may not be
        # a good approach.
        for letter in ransomNote:
            if letter in magazine:
                magazine = magazine.replace(letter, '', 1)
                ran.append(letter)
        if ransomNote == ''.join(ran):
            return True
        return False


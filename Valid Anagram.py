#https://leetcode.com/problems/valid-anagram
#https://leetcode.com/submissions/detail/1043371565/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSet = set(list(s)); tSet = set(list(t))
        if sSet != tSet:
            return False
        for key in sSet:
            if s.count(key) != t.count(key):
                return False
        return True
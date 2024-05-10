#https://leetcode.com/problems/isomorphic-strings/
#https://leetcode.com/submissions/detail/1226982951/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        translationLayerBack = {}
        translationLayerForth = {}
        
        for i, letter in enumerate(s):
            try:
                if translationLayerBack[letter] != t[i]:
                    return False
            except KeyError:
                try:
                    if translationLayerForth[t[i]] != letter:
                        return False
                except KeyError:
                    translationLayerBack.update({letter: t[i]})
                    translationLayerForth.update({t[i]: letter})
                
        return True

s = Solution()

str1 = "egg"; str2 = "add"
print(s.isIsomorphic(str1, str2))

str1 = "badc"; str2 = "baba"
print(s.isIsomorphic(str1, str2))
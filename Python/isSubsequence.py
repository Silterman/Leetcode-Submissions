#https://leetcode.com/problems/is-subsequence/
#https://leetcode.com/submissions/detail/1241623701/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer = 0

        for letter in s:
            while True:
                if pointer >= len(t):
                    return False
                if letter == t[pointer]:
                    pointer += 1
                    break
                pointer += 1

        return True
    
s = Solution()

print(s.isSubsequence("abc", "ahbgdc"))
print(s.isSubsequence("axc", "ahbgdc"))
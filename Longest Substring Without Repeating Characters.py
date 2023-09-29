#https://leetcode.com/problems/longest-substring-without-repeating-characters/
#https://leetcode.com/submissions/detail/1062395537/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = []; longest = 0
        for letter in s: 
            if letter not in unique:
                unique.append(letter)
            else:
                if len(unique) > longest:
                    longest = len(unique)
                unique = unique[unique.index(letter)+1:]
                unique.append(letter)
        return max(len(unique), longest)

s = Solution()
print(s.lengthOfLongestSubstring("ohvhjdml"))
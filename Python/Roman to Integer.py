#https://leetcode.com/problems/roman-to-integer/
#https://leetcode.com/submissions/detail/1062363680/

class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        output = romanDict[s[-1]]
        
        for i in range(len(s)-1):
            if romanDict[s[i]] < romanDict[s[i+1]]:
                output -= romanDict[s[i]]
            else:
                output += romanDict[s[i]]
        return output
    

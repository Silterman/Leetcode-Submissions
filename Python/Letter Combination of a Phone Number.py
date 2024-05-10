#https://leetcode.com/problems/letter-combinations-of-a-phone-number
#https://leetcode.com/submissions/detail/977786147/

class Solution(object):
    def letterCombinations(self, digits):
        output, phoneDict = [], {2:["a", "b", "c"], 3:["d", "e", "f"], 4:["g", "h", "i"], 5:["j", "k", "l"], 6:["m", "n", "o"], 7:["p", "q", "r", "s"], 8:["t", "u", "v"], 9:["w", "x", "y", "z"]}
        
        if digits == "":
            return output
        
        output = phoneDict[int(digits[0])]
        
        for i in digits[1:]:
            newOutput = []
            for letter in output:
                for j in phoneDict[int(i)]:
                    newOutput.append(letter+j)
            output = newOutput
        
        return output
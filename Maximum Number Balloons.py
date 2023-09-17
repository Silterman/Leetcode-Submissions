#https://leetcode.com/problems/maximum-number-of-balloons/
#https://leetcode.com/submissions/detail/1047855292/

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        output = (text.count("b"), text.count("a"), text.count("l")//2, text.count("o")//2, text.count("n"))
        return min(output)
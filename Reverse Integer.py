#https://leetcode.com/problems/reverse-integer
#https://leetcode.com/submissions/detail/1043338907/

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = -1*int(str((x*-1))[::-1])
        else:
            x = int(str(x)[::-1])
        if -2**31 <= x < 2**31:
            return x
        return 0
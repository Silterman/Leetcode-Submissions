#https://leetcode.com/problems/happy-number/
#https://leetcode.com/submissions/detail/1051198293/

class Solution:
    def isHappy(self, n: int) -> bool:
        falseSums = [n]
        while True:
            nList = [int(x) for x in str(n)]
            n = sum(i*i for i in nList)
            if n == 1:
                return True
            if n in falseSums:
                return False
            falseSums.append(n)
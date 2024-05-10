#https://leetcode.com/problems/add-digits/
#https://leetcode.com/submissions/detail/1051206516/

class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            nList = [int(x) for x in str(num)]
            if len(nList) == 1:
                return num
            num = sum(nList)
#https://leetcode.com/problems/fizz-buzz/
#https://leetcode.com/submissions/detail/1233869493/

class Solution(object):
    def fizzBuzz(self, n: int) -> list:
        return ["Fizz"*(i%3==0)+"Buzz"*(i%5==0) or str(i) for i in range(1, n+1)]
    
s = Solution()

print(s.fizzBuzz(3))
#https://leetcode.com/problems/zigzag-conversion
#https://leetcode.com/submissions/detail/984729547/

class Solution:
    def outputConvert(self, l):
        output = ""
        for i in l:
            output += i
        return output
    
    def convert(self, s: str, numRows: int):
        if numRows == 1:
            return s
        output, n = [""]*numRows, 0
        for i in s:
            output[n] += i
            #print(output, n, i)
            if n >= 0:
                if n == numRows-1:
                    n = -2
                    continue
                n += 1
                continue
            if n == -numRows:
                n = 1
                continue
            n -= 1
        return Solution.outputConvert(self, output)
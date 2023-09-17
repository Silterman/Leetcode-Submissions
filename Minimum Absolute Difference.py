#https://leetcode.com/problems/minimum-absolute-difference/
#https://leetcode.com/submissions/detail/1047868206/

class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        minAbsDiff = float('inf')

        for i in range(len(arr)-1):
            x = arr[i]; y = arr[i+1]
            tempAbs = abs(x-y)
            if tempAbs < minAbsDiff:
                minAbsDiff = tempAbs
                output = [[x, y]]
            elif tempAbs == minAbsDiff:
                output.append([x, y])
        return output
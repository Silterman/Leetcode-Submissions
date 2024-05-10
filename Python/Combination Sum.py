#https://leetcode.com/problems/combination-sum
#https://leetcode.com/submissions/detail/1034973063/

class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        results = []
        def helper(i, path):
            print(i, path)
            # endpoint 1 (we found a matching target)
            if sum(path) == target:
                print("result found:",path[:])
                results.append(path[:])
                return 
			
			# endpoint 2 (The sum is greater than the target)
            if sum(path) > target:
                print("greater sum found:", path)
                return False
			
            for x in range(i, len(candidates)):
                path.append(candidates[x])
                helper(x, path)
                path.pop()

        helper(0, [])
        return results
#https://leetcode.com/problems/generate-parentheses
#https://leetcode.com/submissions/detail/977685374/

class Solution(object):
    def generateParenthesis(self, n):
        compList = ["("]
        
        while True:
            newList = []
            for i in compList:
                if i.count("(") > i.count(")") and i.count("(") < n :
                    newList.append(i+")"); newList.append(i+"(")
                elif i.count ("(") == n:
                    newList.append(i+")")
                else:
                    newList.append(i+"(")
                    
            if len(compList) == len(newList):
                return [i+")" for i in newList]
            
            compList = newList
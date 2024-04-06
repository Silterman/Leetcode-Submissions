#https://leetcode.com/problems/the-skyline-problem/description/
#

#way too slow and bloated
class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        skylineDict = {}
        
        if len(buildings) == 1:
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
        
        for building in buildings:
            for x_cood in range(building[0], building[1]):
                if x_cood in skylineDict:
                    skylineDict.update({x_cood:max(building[2], skylineDict[x_cood])})
                else:
                    skylineDict.update({x_cood:building[2]})

        skyline = [[list(skylineDict)[0], skylineDict[list(skylineDict)[0]]]]
        
        for i in range(min(list(skylineDict))+1, max(list(skylineDict))+1):
            try: 
                if skylineDict[i] != skyline[-1][1]:
                    skyline.append([i, skylineDict[i]])
            except KeyError:
                if skyline[-1][1] != 0:
                    skyline.append([i, 0])
            
        skyline.append([max(list(skylineDict))+1, 0])
        
        return skyline
    
s = Solution()

buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
print(s.getSkyline(buildings))

buildings = [[0,1,3]]
print(s.getSkyline(buildings))
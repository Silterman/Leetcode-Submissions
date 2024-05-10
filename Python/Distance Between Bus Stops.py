#https://leetcode.com/problems/distance-between-bus-stops
#https://leetcode.com/submissions/detail/1047849935/

class Solution:
    def distanceBetweenBusStops(self, distance: list[int], start: int, destination: int) -> int:
        if start < destination:
            output = (sum(distance[start:destination]), sum(distance[:start]+distance[destination:len(distance)]))
        else:
            l = len(distance)
            distance = distance*2
            #print(distance)
            output = (sum(distance[start:l+destination]), sum(distance[destination:start]))
            #print(distance[start:l+destination], distance[destination+1:start])
        return min(output)
#https://leetcode.com/problems/number-of-students-unable-to-eat-lunch
#https://leetcode.com/submissions/detail/1226973453/

class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        studentIndex = 0
        sandwhichIndex = 0
        
        studentStartSize = len(students)
        lastChange = 0
        
        while True:
            #exit conditions
            if students[-1] is None: #when all students have eaten
                return 0
            if lastChange > studentStartSize+1: #or when all remaining students have the same preference and the first sandwhich is not prefered
                return studentStartSize - sandwhichIndex
            
            if students[studentIndex] == sandwiches[sandwhichIndex]:
                students[studentIndex] = None
                sandwhichIndex += 1
                studentIndex += 1
                lastChange = 0
            else:
                students.append(students[studentIndex])
                students[studentIndex] = None
                studentIndex += 1
                lastChange += 1
            
s = Solution()
    
students = [1,1,0,0]; sandwiches = [0,1,0,1]
print(s.countStudents(students, sandwiches))

students = [1,1,1,0,0,1]; sandwiches = [1,0,0,0,1,1]
print(s.countStudents(students, sandwiches))
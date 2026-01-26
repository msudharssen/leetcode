"""
1. Count number of students prefering 1, then 0. Total should be length of students
2. go through the sandwiches, each time you see a 1, and the count of 1 > 0, you decrement, do the same you see a 0 with the count of 0
3. return total if neither of these criteia is met, return total right away. Else return total at the end. 
"""
def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
    numberOfOnes = 0
    numberOfZeros = 0
    res = len(students)

    for student in students:
        if student==1:
            numberOfOnes+=1
        else:
            numberOfZeros+=1
    
    for sandwich in sandwiches:
        if sandwich==1 and numberOfOnes>0:
            numberOfOnes-=1
        elif sandwich==0 and numberOfZeros>0:
            numberOfZeros-=1
        else:
            return res
        res-=1
    return res
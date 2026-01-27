"""
1. Go down from top left to bottom right. Keep track of visited cell in a hashset
2. Do the same starting from top right to bottom left. 
3. return the totalSum
"""

def diagonalSum(self, mat: List[List[int]]) -> int:
        runningSum = 0
        info = set()
        rows = len(mat)
        cols = len(mat[0])
        r = 0
        c = 0
        while r < rows and c < cols:
            runningSum+=mat[r][c] if (r,c) not in info else 0
            info.add((r,c))
            c+=1
            r+=1
        print(info)
        
        r = 0
        c = cols-1
        while r<rows and c>=0:
            runningSum+=mat[r][c] if (r,c) not in info else 0
            info.add((r,c))
            r+=1
            c-=1
        return runningSum
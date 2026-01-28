"""
MAX CONSECUTIVE ONES 3

1. Two pointers
2. Keep track of number of zeros
3. if numberOfZeros > k, then enter a while loop, while its greater, decrease the zero, and increase l
4. update length, then return the length at the end
"""

def longestOnes(self, nums: List[int], k: int) -> int:
        numberOfZeros = 0
        l = 0
        res = 0
        for r in range(len(nums)):
            if nums[r]==0:
                numberOfZeros+=1
            while numberOfZeros > k:
                if nums[l] == 0:
                    numberOfZeros -= 1
                l += 1
            res = max(res, r-l+1)
        return res
"""
1. initalize two variables, first, second, both ints, set them to inf
2. update first if you see a value less than first, do the same with second
3. if both conditions in 2 isnt true, return true
4. after the for loop return false
"""

def increasingTriplet(self, nums: List[int]) -> bool:
        
        nums_i = float('inf')
        nums_j = float('inf')

        for num in nums:
            if num <= nums_i:
                nums_i = num
            elif num <= nums_j:
                nums_j = num
            else:
                return True
        return False
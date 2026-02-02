"""
1. keep a hashset
2. iterate through the array, if it breaks the window, move the left pointer up one, but remove that element from hashset first
3. if the element is in info, return True
4. add element to the hashset, return False at the end
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        info = set()
        l = 0

        for r in range(len(nums)):
            if r-l+1 >k+1:
                info.remove(nums[l])
                l+=1
            if nums[r] in info:
                return True
            info.add(nums[r])

        return False
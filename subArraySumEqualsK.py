"""
1. keep a prefix of currSum, and a hashmap of each currSum to its freq., initialize map[0]=1
2. find differnece between currSum - k
3. check if difference exists in hashmap, if so, add its count to result
4. add currSum to hashmap, then return the result at the end
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currSum = 0
        info = defaultdict()
        info[0]=1
        

        for num in nums:
            currSum += num
            diff = currSum - k
            if diff in info:
                res += info[diff]
            if currSum not in info:
                info[currSum]=1
            else:
                info[currSum]+=1
            
        return res
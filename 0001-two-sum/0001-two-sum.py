class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i, val in enumerate(nums):
            key=target-val
            if key in hash:
                return [hash[key],i]
            hash[val]=i
            

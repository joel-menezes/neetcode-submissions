class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, x in enumerate(nums):
            for j in range(len(nums)):
                if j <= i: 
                    continue
                if x + nums[j] == target:
                    return [i, j]
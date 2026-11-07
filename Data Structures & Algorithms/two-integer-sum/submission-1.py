class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, x in enumerate(nums):
            if target - x in nums and nums.index(target - x) != i:
                return [min(nums.index(target - x), i), max(i, nums.index(target - x))]
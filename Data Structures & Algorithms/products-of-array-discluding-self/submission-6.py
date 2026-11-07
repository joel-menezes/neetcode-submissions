class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        b = []
        for i in range(len(nums)):
            a = 1
            for j in nums[:i]:
                a *= j
            for j in nums[i + 1:]:
                a *= j
            b.append(a)
        return b
            

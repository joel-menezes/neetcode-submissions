class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        b = 1
        a = []
        for i in nums:
            if i != 0:
                b*=i
        if nums.count(0) > 1:
            return [0 for _ in range(len(nums))]
        elif nums.count(0) == 1:
            
            for i in nums:
                if i != 0:
                    a.append(0)
                else:
                    a.append(b)
        else:
            for i in nums:
                print(b)
                a.append(b//i)
        return a
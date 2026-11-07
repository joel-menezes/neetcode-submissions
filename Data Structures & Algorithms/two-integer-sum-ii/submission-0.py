class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        l = 0
        r = len(numbers) - 1
        
        while l <= r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            else:
                if numbers[r] > target - numbers[l] :
                    r -= 1
                else:
                    l += 1
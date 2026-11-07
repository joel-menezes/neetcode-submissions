class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            if target == nums[low]:
                return low
            elif target == nums[high]:
                return high
            elif target == nums[mid]:
                return mid
            else:
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
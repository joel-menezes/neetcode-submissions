class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums[:]
        else:
            middle = len(nums) // 2
            left = self.sortArray(nums[:middle])
            right = self.sortArray(nums[middle:])

            return self._merge(left, right)

    def _merge(self, left: List[int], right: List[int]) -> List[int]:
        l = 0
        r = 0
        lst = []
        while l < len(left) or r < len(right):
            if l == len(left):
                lst.append(right[r])
                r += 1
            elif r == len(right):
                lst.append(left[l])
                l += 1
            elif left[l] <= right[r]:
                lst.append(left[l])
                l += 1
            else:
                lst.append(right[r])
                r += 1

        return lst
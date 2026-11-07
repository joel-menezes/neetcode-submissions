class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        i = len(digits) - 1
        while digits[i] > 9:
            digits[i] -= 10
            if digits[i - 1]:
                digits[i - 1] += 1
            else:
                digits.insert(0, 1)
            i -= 1
        return digits
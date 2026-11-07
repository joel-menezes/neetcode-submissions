class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        elif n == 0:
            return False
        else:
            if n % 2 != 0:
                return False
            return self.isPowerOfTwo(n >> 1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0
        else:
            if n & 1 == 1:
                return 1 + self.hammingWeight (n >> 1)
            else:
                return self.hammingWeight (n >> 1)
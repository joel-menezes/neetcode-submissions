class Solution:
    def reverseBits(self, n: int) -> int:
        a = 0
        for i in range(32):
            a = (a << 1 | n & 1)
            n >>=  1

        return a
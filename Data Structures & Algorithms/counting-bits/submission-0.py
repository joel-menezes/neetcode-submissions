class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(n + 1):
            arr.append(self.bits(i))
        return arr

    def bits(self, n: int) -> int:
        if n == 0:
            return 0
        else:
            if n & 1 == 1:
                return 1 + self.bits(n >> 1)
            else:
                return self.bits(n >> 1)
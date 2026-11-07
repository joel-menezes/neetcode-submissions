class Solution:
    def isPalindrome(self, s: str) -> bool:
        # a = ""
        # for i in s:
        #     if i.isalpha() or i.isdigit():
        #         a += i.lower()
        # return a==a[::-1]
        a = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                a += i.lower()
        l = 0
        r = len(a) - 1
        while l <= r:
            if not a[l] == a[r]:
                return False
            l += 1
            r -= 1
        return True
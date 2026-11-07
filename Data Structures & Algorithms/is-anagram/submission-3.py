class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_, t_ = {}, {}

        for i in range(len(s)):
            s_[s[i]] =  1 + s_.get(s[i], 0)
            t_[t[i]] =  1 + t_.get(t[i], 0)
        
        return s_ == t_
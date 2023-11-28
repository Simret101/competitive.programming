class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict={}
        res,l=0,0
        for r in range(len(s)):
            if s[r] in dict:
                l=max(l,dict[s[r]]+1)
            dict[s[r]]=r
            res=max(res,r-l+1)
        return res
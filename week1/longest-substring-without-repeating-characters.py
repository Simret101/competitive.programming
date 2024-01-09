class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict={}
        l,r=0,0
        res=0
        while r<len(s):
            if s[r] in dict:
                l=max(l,dict[s[r]]+1)
            dict[s[r]]=r      
            res=max(res,r-l+1)
            r+=1       
        return res
       
        
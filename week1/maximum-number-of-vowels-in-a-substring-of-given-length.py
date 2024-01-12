class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ans={'a','e','i','o','u'}
        l=0
        count=0
        res=0
        for r in range(len(s)):
            if s[r] in ans:
               count+=1
            while r-l+1>k:
                if s[l] in ans:
                    count-=1
                l+=1
            res=max(res,count)
        return res
        
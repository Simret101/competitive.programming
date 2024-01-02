class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        ans=""
        for i in range(len(s)):
            if s[i].isalnum():
                ans+=s[i]
        l=0
        r=len(ans)-1
        while l<r:
            if ans[l] != ans[r]:
                return False
            r-=1
            l+=1
        return True
        
       
        
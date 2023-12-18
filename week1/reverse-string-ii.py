class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
   
        s=list(s)
      
        i=0
        while i<len(s):
            s[i:i+k]=reversed(s[i:i+k])
            i=i+(2*k)
        return "".join(s)
        
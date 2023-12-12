class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        x=s.strip()
        ans=x.split()
        rev=ans[::-1]
        return ' '.join(rev)
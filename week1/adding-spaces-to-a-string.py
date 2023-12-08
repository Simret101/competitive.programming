class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        ans=[]
        last=0
        for i in spaces:
            ans.append(s[last:i])
            ans.append(" ")
            last=i
        ans.append(s[last:])
        return "".join(ans)
        
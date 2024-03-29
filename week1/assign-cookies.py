class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        i,j=0,0
        count=0
        g.sort()
        s.sort()
        while i<len(g) and j<len(s):
            if g[i] <=s[j]:
                count+=1
                i+=1
                j+=1
            else:
                j+=1
        return count
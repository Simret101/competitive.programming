class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        l=0
        r=len(skill)-1
        res=0
        tot=skill[l]+skill[r]
        while l<r:
            if skill[l]+skill[r]==tot:
                res+=skill[l]*skill[r]
                l+=1
                r-=1
            else:
                return -1
        return res 
                
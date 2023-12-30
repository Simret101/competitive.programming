class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        l=0
        r=len(piles)-1
        piles.sort()
        tot=0
        while l<=r:
            tot+=piles[r-1]
            l+=1
            r-=2
        return tot

   

       
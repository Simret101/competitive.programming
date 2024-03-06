class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=0,max(piles)
        res=r
        def helper(mid):
            cur_mid=mid
            count=0
            
            for i in piles:
                count+=ceil(i/cur_mid)
                
                
            return (h-count>=0)
        while l+1<r:
            mid=(l+r)//2
            if helper(mid):
                
                r=mid
            else:
                l=mid
        return r

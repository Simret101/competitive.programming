class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        res=r
        def helper(mid):
            ships,cur_mid=1,mid
            for i in weights:
                if cur_mid-i<0:
                    ships+=1
                    cur_mid=mid
                cur_mid-=i
            return ships<=days
        while l<=r:
            mid=(l+r)//2
            if helper(mid):
                res=min(res,mid)
                r=mid-1
            else:
                l=mid+1
        return res
        


















class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        r = max(nums)
        res = max(nums)
        
        def helper(mid):
            tot = 0
            
            for i in nums:
                tot += ceil(i /mid)  
            return tot <= threshold
        
        while l <= r:
            mid = (l + r) // 2
            if helper(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res
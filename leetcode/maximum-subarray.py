class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
     
        res = nums[0]
        tot = nums[0]  
        
        for i in range(1, len(nums)):
            if tot < 0:
                tot = nums[i]  
            else:
                tot += nums[i] 
            
            res = max(res, tot)
        
        return res

        
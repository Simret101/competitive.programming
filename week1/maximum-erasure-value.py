class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        tot=0
        ans=set()
        r=0
        res=0
        r,l=0,0
        while r<len(nums):          
            if nums[r] not in ans :
                ans.add(nums[r])
                tot+=nums[r]
                r+=1
            else:
                tot-=nums[l]
                ans.remove(nums[l]) 
                l+=1 
            res=max(res,tot)      
        return res
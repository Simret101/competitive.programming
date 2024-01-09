class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if target>sum(nums):return 0
        res=len(nums)+1
        l,r=0,0
        tot=0
        while r<len(nums):
            tot+=nums[r]
            while tot>=target:
                res=min(res,r-l+1)
                tot-=nums[l]
                l+=1
            r+=1
        return res

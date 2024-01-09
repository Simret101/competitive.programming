class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l,r,count=0,0,0
        res=0
        while r<len(nums):
            if nums[r]==0:
                count+=1
            while count>k:
                if nums[l]==0:
                    count-=1
                l+=1
            res=max(res,r-l+1)
            r+=1
        return res

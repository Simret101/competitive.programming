class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=1
        l,r=0,0
        res=0
        while r<len(nums):
            if nums[r]==0:
                count-=1  
            while count<0:
                if nums[l]==0:
                    count+=1
                l+=1
            r+=1 
            res=max(res,r-l-1)
            
           
                
        return res

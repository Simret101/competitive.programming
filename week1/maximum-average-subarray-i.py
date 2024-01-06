class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        res=[]
        l=0
        r=k
        tot=sum(nums[l:r])
        res=tot/float(k)
        while r<len(nums):
            tot-=nums[l]
            tot+=nums[r]
            res=max(res,tot/float(k))
            l+=1
            r+=1
        return res
        
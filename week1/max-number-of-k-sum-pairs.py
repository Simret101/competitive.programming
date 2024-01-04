class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        count=0
        l=0
        r=len(nums)-1
        while l<r:
            sum=nums[l]+nums[r]
            if sum>k:
                r-=1
            elif sum<k:
                l+=1
            else:
                count+=1
                l+=1
                r-=1
        return count
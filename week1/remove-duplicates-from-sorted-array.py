class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=l+1
        count=0
        while r<len(nums):
            if nums[l]==nums[r]:
                r+=1
            else:
                l+=1
                nums[l]=nums[r]
                count+=1
        return count + 1

        
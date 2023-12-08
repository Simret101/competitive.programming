class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=0
        for i in range(len(nums)+1):
            if i in nums:
                continue
            else:
                x=i
        return x

        
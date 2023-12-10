class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        dict1={}
        for i ,j in enumerate(nums):
            dict1[j]=i
        for x,y in operations:
            before=dict1[x]
            nums[before]=y
            dict1[y]=before
            del dict1[x]
          

        return nums


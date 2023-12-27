class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ordered_nums=sorted(nums)
        ans=[]
        for i in nums:
            ans.append(ordered_nums.index(i))
        return ans
      
      
            


        
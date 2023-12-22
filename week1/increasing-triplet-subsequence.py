class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first_min=float('inf')
        second_min=float('inf')
        for i in range(len(nums)):
           
            if nums[i]<first_min:
                first_min=nums[i]
            elif nums[i]>first_min and nums[i]<second_min:
                second_min=nums[i]
            elif nums[i]>second_min:
                return True
        
        return False
      
        
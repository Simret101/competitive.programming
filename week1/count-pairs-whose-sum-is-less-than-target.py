class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        count=0
        
        for i in range(len(nums)):
            r=len(nums)-1
            while r>i:
                if nums[i] + nums[r] < target:
                    count+=1
                r-=1
        return count
                    


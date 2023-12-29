class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # counter = Counter(nums)
        # nums.sort()
        # x = set(nums)
        # nums = list(x)
        # n = len(nums)
        # count = 0
        
        # for r in range(n-1, 0, -1):
        #     n = r * counter[nums[r]]
        #     count += n
        
        # return count
        
        nums.sort()
        n = len(nums)
        l = n - 2
        count = 0
        
        while l >= 0:
            if nums[l] < nums[l + 1]:
                count += n - l - 1
            l -= 1
        
        return count
       




      
            

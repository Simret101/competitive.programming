class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        total_sum = sum(num for num in nums if num % 2 == 0)
        res = []
        for i in range(len(queries)):
            x, y = queries[i]
            if nums[y] % 2 == 0:
                total_sum -= nums[y] 
            nums[y] += x 
            if nums[y] % 2 == 0:
                total_sum += nums[y]
            res.append(total_sum)
        
        return res
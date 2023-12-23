class Solution(object):
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=max_res=sum(nums)
        ans=[0]
        for i,val in enumerate(nums,1):
            res += 1 if val == 0 else -1
            if res > max_res:
                ans = [i]
                max_res = res
            elif res == max_res:
               ans.append(i)
        
        return ans
        
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num=set(nums)
        tot=0
        for i in num:
            if i-1 not in num:
                beg=i
                while beg in num:
                    beg+=1
                tot=max(tot,beg-i)
        return tot

       
         
   



        
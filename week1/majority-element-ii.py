class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        dict={}
        for i in nums:
            dict[i]=dict.get(i,0)+1
            if dict[i]>len(nums)//3 and i not in res:
                res.append(i)
        return res
            
            


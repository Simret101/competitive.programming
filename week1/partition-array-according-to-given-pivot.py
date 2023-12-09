class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        less_pivot=[]
        greater_pivot=[]
        equal_pivot=[]
        for i in nums:
            if i<pivot:
                less_pivot.append(i)
            elif i>pivot:
                greater_pivot.append(i)
            elif i==pivot:
                equal_pivot.append(i)
       
        return less_pivot+ equal_pivot + greater_pivot



        
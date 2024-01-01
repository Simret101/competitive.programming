class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        flips=[]
        cur_max=len(arr)
        for i in range(len(arr)):
            cur_max_index=arr.index(cur_max)
            arr[:cur_max_index+1]=arr[:cur_max_index+1][::-1]
            flips.append(cur_max_index+1)
            arr[:cur_max]=arr[:cur_max][::-1]
            flips.append(cur_max)
            cur_max-=1
        return flips
       
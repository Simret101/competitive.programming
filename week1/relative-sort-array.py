class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        store_unsorted=defaultdict(int)
        remain=[]
        sorted_half=[]
        for i in arr1:
            store_unsorted[i]=store_unsorted.get(i,0)+1
            if i not in arr2:
                remain.append(i)
        remain.sort()
        for i in arr2:
            for j in range(store_unsorted[i]):
                sorted_half.append(i)
        return sorted_half + remain



        
class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        return Counter(arr).most_common(1)[0][0]
     



        
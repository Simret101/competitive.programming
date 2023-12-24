class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr)<3:
            return False
        l=0
        r=len(arr)-1
        while l<r and arr[l]< arr[l+1]:
                l+=1
        if l==0 or l==r:
            return False
        while l<r and arr[l]>arr[l+1]:
                l+=1
        return l==r
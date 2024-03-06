class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=-1
        r=len(nums)-1
        while l+1<r:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid
            else:
                r=mid
        return nums[r]
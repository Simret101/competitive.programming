class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            x=bisect_right(nums,target)-1
            
        else:
            x=bisect_right(nums,target)
        return x
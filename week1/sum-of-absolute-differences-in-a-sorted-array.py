class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        tot=sum(nums)
        right=0
        left=0
        res=[]
        for i in range(len(nums)):
            right=tot-left-nums[i]
            res.append(((nums[i]*i)-left)+(right-(len(nums)-i-1)*nums[i]))
            left+=nums[i]
        return res
      
            
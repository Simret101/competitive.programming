class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        tot=0
        ans=[]
        for i in range(len(nums)):
            tot+=nums[i]
            ans.append(tot)
        return ans


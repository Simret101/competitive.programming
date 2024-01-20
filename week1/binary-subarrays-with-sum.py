class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dict={0:1}
        tot=0
        ans=0
        for i in range(len(nums)):
            tot+=nums[i]
            ans+=dict.get(tot-goal,0)
            dict[tot]=dict.get(tot,0)+1
        return ans

            
            

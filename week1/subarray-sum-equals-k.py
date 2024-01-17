class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dict={0:1}
        tot=0
        ans=0
        for i in range(len(nums)):
            tot+=nums[i]
            ans+=dict.get((tot-k),0)
            dict[tot]=dict.get(tot,0)+1
        return ans
      
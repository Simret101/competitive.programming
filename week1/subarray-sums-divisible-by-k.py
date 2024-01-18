class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dict={0:1}
        tot=0
        ans=0
        for i in range(len(nums)):
            tot+=nums[i]
            if tot%k in dict:
                ans+=dict.get(tot%k,0)
                dict[tot%k]+=1
            else:
                dict[tot%k]=dict.get(tot%k,0)+1

        return ans
        

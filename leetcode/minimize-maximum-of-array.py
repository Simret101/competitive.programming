class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans=[]
        tot=0
        for i in range(len(nums)):
            tot+=nums[i]
            x=i+1
            ans.append(ceil(tot/x))
        return max(ans)

            
            
       


     




        
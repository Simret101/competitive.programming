class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        ans1=[0]
        tot1=0
        res=0
        
        for i in range(len(nums)):
            tot1+=nums[i]
            ans1.append(tot1)
        for j in range(1,len(ans1)):
            if ans1[j-1]==ans1[-1]-ans1[j]:
                return j-1
        return -1
        

           
        
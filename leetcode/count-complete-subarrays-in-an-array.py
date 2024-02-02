class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        x=set(nums)
        dict={}
        l,r=0,0
        count=0
        res=0
        while r<len(nums):
            if nums[r] not in dict:
                dict[nums[r]]=0
            dict[nums[r]]+=1
            while len(dict)==len(x):
                count+=1
                dict[nums[l]]-=1
                if dict[nums[l]]==0:
                    del dict[nums[l]]
                l+=1
            res+=count
            r+=1
        return res
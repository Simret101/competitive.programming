class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    
        l, r = 0, 0
        count = 0
        ans=0
        res_sub =0
        for r in range(len(nums)):
            if nums[r] % 2 == 1:
                count += 1
                res_sub=0
            while count == k:
                if nums[l] % 2 == 1:
                    count -= 1
                res_sub+=1
                l += 1
            ans+=res_sub
        return ans
                
       
            


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        nums.sort()
       
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            l=i+1
            r=len(nums)-1
            while l<r:
                sum=nums[l]+nums[r]+nums[i]
                if sum>0:
                    r-=1
                elif sum<0:
                    l+=1
                else:
                    ans.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return ans
                    
    
                    
        

   
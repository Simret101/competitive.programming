class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int          
        :rtype: int
        """
        nums.sort()
        res=sum(nums[:3])
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                tot=nums[i]+nums[l]+nums[r]
                if abs(tot-target)<abs(res-target):
                    res=tot
                if tot>target:
                    r-=1
                elif tot<target:
                    l+=1
                else:
                    return res
                    l+=1
                    r-=1
              
        return res if res else 0

        
       
      
                


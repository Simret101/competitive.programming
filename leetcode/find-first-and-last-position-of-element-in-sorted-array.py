class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums==[] or target not in nums:
            return [-1,-1]
        ans=[]
        x=bisect_left(nums,target)
        y=bisect_right(nums,target)-1
     
        return [x,y]
        # res=[-1,-1]
        # ans=0
        # l=0
        # r=len(nums)-1
   
        # while l<=r:
        #     mid=(l+r)//2
        #     if nums[mid]>target:
        #         l=mid-1
        #     elif nums[mid]>target:
        #         r=mid+1
        #     else:
        #         ans=mid
        #         res[0]=mid
                
        # l=0
        # r=ans   
        # while l<=r:
           
        #     mid=(l+r)//2
        #     if nums[mid]>target:
        #         l=mid-1
        #     elif nums[mid]>target:
        #         r=mid+1
        #     else:
        #         ans=mid
        
        #         res[1]=mid
        # return res
         
           


      
                
                


                   
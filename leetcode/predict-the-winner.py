class Solution:
    def helper(self,nums,l,r,flag):
        if l==r:
            return nums[l]

            
        else:
            if flag:
                if l==r:
                    return nums[l]
                left=self.helper(nums,l+1,r,False)+nums[l]

                right= self.helper(nums,l,r-1,False)+nums[r]
                return max(left,right)

            else:
                if l==r:
                    return  -nums[l]
                left=self.helper(nums,l+1,r,True)-nums[l]

                right=self.helper(nums,l,r-1,True)-nums[r]
                return min(left,right)

    def predictTheWinner(self, nums: List[int]) -> bool:
        return self.helper(nums,0,len(nums)-1,True)>=0
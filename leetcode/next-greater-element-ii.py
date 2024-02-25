class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        n=len(nums)
        ans=[-1]*n
        
     
        for i in range(0,n*2):
            while stack and nums[stack[-1]]<nums[i%n]:
                x=stack.pop()
                ans[x]=nums[i%n]
            if i<n:
                stack.append(i%n)
        return ans
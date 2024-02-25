class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        ans={}
        res=[]
        for i in range(len(nums2)):
            
            while stack and stack[-1] < nums2[i]:
                x=stack.pop()
                ans[x]=nums2[i]
            stack.append(nums2[i])
            
        while stack:
            x=stack.pop()
            ans[x]=-1
           
            
            
        for i in nums1:
            res.append(ans[i])
        return res

        


       
       
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
       
        def helper(num,path):
           
            ans.append(path[:])
            for i in range(num,len(nums)):
                path.append(nums[i])
                helper(i+1,path)
                path.pop()
            
        ans=[]
        helper(0,[])
        return ans


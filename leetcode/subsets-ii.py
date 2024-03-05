class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        path=[]
        def helper(num):
            if path not in ans:
                ans.append(path[:])
            for i in range(num,len(nums)):
                
                path.append(nums[i])
                helper(i+1)
                path.pop()
        helper(0)
        return ans

            
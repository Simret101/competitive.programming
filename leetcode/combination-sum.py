class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(num,path,target):
            if target==0:
                ans.append(path[:])
            if target<0:
                return
               
                
            for i in range(num,len(candidates)):
                path.append(candidates[i])
        
                helper(i,path,target-candidates[i])

                path.pop()
            return ans

        ans=[]
   
        return helper(0,[],target)
         
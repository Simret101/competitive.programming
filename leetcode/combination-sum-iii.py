class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        path=[]
        def helper(num,n,k):
            if len(path)==k and sum(path)==n:
                ans.append(path[:])
            
            for i in range(num,10):
                path.append(i)
                helper(i+1,n,k)
                path.pop()
        helper(1,n,k)
        return ans
            
            
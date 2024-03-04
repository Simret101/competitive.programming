class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(num,path):
            if len(path)==k:
                ans.append(path[:])
                return
            for i in range(num,n+1):
                path.append(i)
                helper(i+1,path)
                path.pop()
        ans=[]
        helper(1,[])
        return ans
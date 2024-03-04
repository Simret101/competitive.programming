class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        child=[0]*k
        min_un=float(inf)

        def helper(i):
            nonlocal min_un
            
            if i==len(cookies):
                un=max(child)
                min_un=min(min_un,un)
                return
            for j in range(k):
                child[j]+=cookies[i]
                if child[j] < min_un:
                    helper(i+1)
                child[j]-=cookies[i]
            
        helper(0)
        return min_un
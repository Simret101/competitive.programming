class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans=Counter(t)
        r,l=0,0
        n=len(ans)
        res=""
        while r<len(s):
            if s[r] in ans:
                ans[s[r]]-=1
                if ans[s[r]]==0:
                    n-=1
            while n==0:
                if not res:
                    res=s[l:r+1]
                elif r-l+1<len(res):
                    res=s[l:r+1]
                if s[l] in ans:
                    ans[s[l]]+=1
                    if ans[s[l]]>0:
                        n+=1
                l+=1
            r+=1
        return res

          

        
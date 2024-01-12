class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        store=defaultdict(str)
        l,r=0,0
        res=0
        while r<len(s):
            store[s[r]]=store.get(s[r],0)+1
            while (r-l+1-max(store.values()))>k:
                store[s[l]]-=1
                if store[s[l]]==0:
                    del store[s[l]]
                l+=1
            res=max(res,r-l+1)
            r+=1
        return res
            



        
      
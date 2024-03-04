from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dict={}
        for i in range(len(s)):
            dict[s[i]]=i
        l,r=0,0
        res=[]
        for i in range(len(s)):
            r=max(r,dict[s[i]])
            if r==i:
                res.append(r-l+1)
                l=i+1
        return res
        
                
                
           
        
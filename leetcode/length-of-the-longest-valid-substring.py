class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        ans=set(forbidden)
        l,res=0,0
        for i in range(len(word)):
            for j in range(i,max(i-10,l-1),-1):
                if word[j:i+1] in ans:
                    l=j+1
                    break
            res=max(res,i-l+1)
        return res
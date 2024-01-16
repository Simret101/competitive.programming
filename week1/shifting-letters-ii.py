class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ans=[0]*(len(s)+1)
        for start,end,dir in shifts:
            ans[start]+=1 if dir==1 else -1
            ans[end+1]-=1 if dir==1 else -1
    
        for i in range(1,len(s)+1):
            ans[i]+=ans[i-1]
        tot1=[]
        for i,ans in enumerate(ans[:-1]):
            pos=ascii_lowercase.index(s[i])
            res=(pos+ans)%26
            pos1=ascii_lowercase[res]
            tot1.append(pos1)
        return ''.join(tot1)



      
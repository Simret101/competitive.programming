class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        ans=[]
        count=0

        for i in range(len(s)):
            if s[i]=='(':
                ans.append('(')
            elif s[i] ==')':
                if ans and ans[-1]=='(':
                    ans.pop()
                else:
                    count+=1
        return count+len(ans)
   

        
                    
class Solution:
    def decode(self,s,i):
        ans=""
        k=0
        while i<len(s):
            if s[i].isdigit():
                k=k*10+int(s[i])
            elif s[i]=='[':
                res,i=self.decode(s,i+1) 
                ans+=res*k
                k=0
            elif s[i]==']':
                return ans,i
            else:
                ans+=s[i]
            i+=1
        return ans,i
   
    
    def decodeString(self, s: str) -> str:
        
        res, _= self.decode(s,0)
        return res
                
        
        
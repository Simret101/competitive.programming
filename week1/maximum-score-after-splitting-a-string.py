class Solution:
    def maxScore(self, s: str) -> int:
        zero=[0]*(len(s)+1)
        one=[0]*(len(s)+1)
        res=0
        for i in range(len(s)):
            if s[i]=='0':
                zero[i]+=zero[i-1]+1
            else:
                zero[i]=zero[i-1]
        for i in range(len(s)-1,-1,-1):
            if s[i]=='1':
                one[i]+=one[i+1]+1
            else:
                one[i]=one[i+1]
        for i in range(len(s)-1):
            tot=zero[i]+one[i+1]
            res=max(res,tot)
        return res



        
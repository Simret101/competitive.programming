class Solution:
    def splitString(self, s: str) -> bool:
        arr=[]
        def helper(start):
            if start==len(s):
                return (len(arr)>=2)
            for i in range(start,len(s)):
                m=int(s[start:i+1])
                if arr and arr[-1]-m!=1:
                    continue
                arr.append(m)
                if helper(i+1):
                    return True
                arr.pop()
            return False
        return helper(0)

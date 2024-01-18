class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        x=0
       
        for i in trips:
            x=max(x,i[2])
        ans=[0]*(x+1)
        for num,start,end in trips:
            ans[start]+=num 
            ans[end]-=num
        for i in range(1,len(ans)):
            ans[i]+=ans[i-1]
        for i in range(len(ans)):
            if ans[i]>capacity:
                return False
        return True


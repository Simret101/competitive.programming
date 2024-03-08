class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        store={interval[0]:i for i,interval in enumerate(intervals)}
        sorted_interval=sorted(interval[0] for interval in intervals )
        n=len(intervals)
        res=[]
        for s,e in intervals:
            ans=e
            idx=bisect_left(sorted_interval,ans)
            if idx==n:
                res.append(-1)
            else:
                val=sorted_interval[idx]
                res.append(store[val])
        return res
       
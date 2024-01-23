class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n=len(nums)
        count=[0]*(len(nums)+1)
        for start,end in requests:
            count[start]+=1
            count[end+1]-=1
        for i in range(1,n+1):
            count[i]+=count[i-1]
        res=0
        nums.sort(reverse=True)
        count.sort(reverse=True)
        for num,req in zip(nums,count):
            res+=num*req
        return res% (10**9+7)
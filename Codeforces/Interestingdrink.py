import bisect
t=int(input())
arr=list(map(int,input().split()))
arr.sort()
n=int(input())

for _ in range(n):
    x=int(input())
   
    
   
    
    ans=bisect.bisect_right(arr,x)
    
        
    print(ans)
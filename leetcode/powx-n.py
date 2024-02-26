class Solution:
    def helper(self,x,y,mod):
        if y==1:
            return x
        if y==0:
            return 1
        if y<0:
            y=0-y
            return (1/(self.helper(x,y,mod)))
  
        if y%2==0:
            val=self.helper(x,y//2,mod) 
            return (val*val)
        else:
            val=self.helper(x,y//2,mod) 
            return (val*val*x)

    



    def myPow(self, x: float, n: int) -> float:
        mod=10**9+7
        return self.helper(x,n,mod)
        
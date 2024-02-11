class Solution:
    def numberOfWays(self, s: str) -> int:
        
        tot=0
        n = len(s)
        zero = s.count('0')
        one = s.count('1')
        pre_zero=0
        pre_one=0
        for i in range(n):
            if s[i] == '0':
                
                tot+= pre_one*(one-pre_one)
                pre_zero+=1
            else:
                tot+= pre_zero*(zero-pre_zero)
                pre_one+=1

       
        return tot
  
        
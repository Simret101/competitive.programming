from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        n=len(s)
        x=Counter(s)
        count=0
        flag=False
        for i in x.keys():
            if x[i]%2==1 and flag==False:
                flag=True
                continue
            if x[i]%2==1 and flag==True:
                n-=1
            
       
        return n

            
                

       

        
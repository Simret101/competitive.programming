class Solution:
    def breakPalindrome(self, palindrome: str) -> str:

        p=list(palindrome)
        n=len(p)//2
        if len(p)==1 :
            return ""


        for i in range(n):
            if p[i]!='a':
                p[i]='a'
                break
        else:
            p[-1]='b'
        return ("".join(p))
        
            

          
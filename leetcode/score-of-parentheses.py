class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        count=0
        res=0
        for i in s:
            if i =='(':
                stack.append(i)
            elif i ==')':
                if stack[-1]=='(':
                    stack.pop()
                    stack.append(1)
                else:
                    res=0
                    while stack[-1]!='(':
                        res+=stack.pop()
                    stack.pop()
                    stack.append(res*2)
                    
        return sum(stack)
class Solution:
    def simplifyPath(self, path: str) -> str:
        dir=path.split('/')
        stack=[]
        for i in dir:
            if i=='.' or not i:
                continue
            
            elif i=='..':
                if stack:
                    stack.pop()
        
            else:
                stack.append(i)
        return ("/" + "/".join(stack))




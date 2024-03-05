class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        path=[]
        def helper(left_p,right_p):
            if left_p==right_p==n:
                ans.append(''.join(path[:]))
            if left_p<n:
                path.append('(')
                helper(left_p+1,right_p)
                path.pop()
            if right_p<left_p:
                path.append(')')
                helper(left_p,right_p+1)
                path.pop()
        helper(0,0)
        return ans

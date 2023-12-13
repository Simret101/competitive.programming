class Solution(object):
    def minimizedStringLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_string={}
        for i in range(len(s)):
            if i in count_string:
                count_string[s[i]]=count_string.get(s[i],0)+1
            else:
                count_string[s[i]]=1
        ans=[]
        for i in count_string:
            if count_string[i] == 1:
                ans.append(i)
        return len(ans)
                

                

                


        
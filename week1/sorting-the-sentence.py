class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        # res=[]
        # arr=list(s.split())
        # arr=sorted(arr, key=lambda x: int(x[-1]))
         
        # for word in arr:
        #     res.append(word[:-1])
        # return ' '.join(res)
        ans=s.split()
        dict={}
        res=[]
        for i in ans:
            index=int(i[-1])
            dict[index]=i[:-1]
        for i in range(1,len(ans)+1):
            res.append(dict[i])
        return ' '.join(res)
            

    

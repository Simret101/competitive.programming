class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        # x=Counter(answerKey)
        # y=x.most_common(1)[0][0]
        # print(y)
        # l,r=0,0
        # res=0
        # count=0
        def solution(chr):
            l,r=0,0
            res=0
            count=0

            while r<len(answerKey):
                if answerKey[r]!=chr:
                    count+=1
                while count>k:
                
                    if answerKey[l]!=chr:
                        count-=1
                    l+=1
                res=max(res,r-l+1)    
                r+=1
            return res
        x=solution("T")
        y=solution("F")

        return(max(x,y))
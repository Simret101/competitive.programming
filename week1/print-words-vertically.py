class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        w= list(s.split(" "))
        n= len(max(w,key=len))
        x=[]
        for i in range(n): 
            curr_word = []
            count_space=0
            for j in range(len(w)):
                if i >= len(w[j]):
                    count_space+=1
                else:
                    curr_word.append(" "*count_space + w[j][i])
                    count_space = 0

            x.append(''.join(curr_word))
        return x

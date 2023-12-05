class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        dict={char:index for index,char in enumerate(order)}
        for i in range(len(words)-1):
            w1,w2=words[i],words[i+1]
            for j in range(len(w1)):
                if j==len(w2):
                    return False
                else:
                    if w1[j]!=w2[j]:
                        if dict[w2[j]]< dict[w1[j]]:
                            return False
                        break
        return True
        
class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        str1=""
        str2=""
        i,j=0,0
        while i<len(word1):
            str1+=word1[i]
            i+=1
        while j<len(word2):
            str2+=word2[j]
            j+=1
        if str1==str2:
            return True
        else:
            return False
        
        


        
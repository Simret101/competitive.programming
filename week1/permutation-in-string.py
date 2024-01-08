class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        dict1={}
        for i in s1:
            dict1[i]=dict1.get(i,0)+1
        l=0
        for r in range(len(s2)):
            seq=s2[l:l+len(s1)]
            dict2={}
            for i in seq:
                dict2[i]=dict2.get(i,0)+1
            if dict2==dict1:
                return True
            l+=1
        return False
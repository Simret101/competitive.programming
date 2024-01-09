class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        if len(p)>len(s): return []
        dict1={}
        dict2={}
        for i in range(len(p)):
            dict1[p[i]]=dict1.get(p[i],0)+1
            dict2[s[i]]=dict2.get(s[i],0)+1
        res=[0] if dict1==dict2 else []
        l=0
        for r in range(len(p),len(s)):
            dict2[s[r]]=dict2.get(s[r],0)+1
            dict2[s[l]]-=1
            if dict2[s[l]]==0:
                dict2.pop(s[l])
            l+=1
            if dict1==dict2:
                res.append(l)
        return res
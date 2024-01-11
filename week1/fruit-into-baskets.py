class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
       
        l,res,tot=0,0,0
        dict={}
        for r in range(len(fruits)):
            dict[fruits[r]]=dict.get(fruits[r],0)+1
            tot+=1
            while len(dict)>2:
                tot-=1
                dict[fruits[l]]-=1
                if dict[fruits[l]]==0:
                    dict.pop(fruits[l])
                l+=1
            res=max(res,tot)
        return res
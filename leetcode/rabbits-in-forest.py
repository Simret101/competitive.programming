from collections import Counter
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        x=Counter(answers)
        ans=[]
        for key in x.keys():
            tot=ceil(((x[key])/(key+1)))*(key+1)
            ans.append(tot)
        return sum(ans)


        # dict=defaultdict()
        # dict[answers[0]]=1
        # tot=answers[0]+1
        # for i in range(1,len(answers)):
            
        #     if answers[i]!=0 and answers[i] in dict:
        #         if dict[answers[i]]<=answers[i]:
        #             tot=tot
        #             dict[answers[i]]+=1
                

                    
        #         elif dict[answers[i]]>answers[i]:
        #             if dict[answers[i]]==answers[i]+1:
        #                 dict[answers[i]]=1
        #                 tot+=answers[i]+1
                    
                 
                   
        #             dict[answers[i]]-=1
        #     else:
        #         dict[answers[i]]=1
        #         tot+=answers[i]+1
        # return tot


        # answers.sort()
        # tot=answers[0]+1
        # count=0
        # for i in range(1,len(answers)):
        #     if answers[i-1]!=0 and answers[i-1]==answers[i]:
        #         count+=1
        #         if count<=answers[i]:

        #             tot=tot
        #         else:
        #             tot+=answers[i]+1
        #     else:
        #         tot+=answers[i]+1
        # return tot
        
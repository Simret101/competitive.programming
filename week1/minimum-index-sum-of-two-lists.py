class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        res=[]
        count = {}
        x=float('inf')

        for i in range(len(list1)):
            count[list1[i]] = i
        count2={}
        for j in range(len(list2)):
            count2[list2[j]] = j
            if list2[j] in count:
                x=min(x,count[list2[j]]+count2[list2[j]])
        for i in count:
            if i in count2:
                score=count[i]+count2[i]
                if score==x:
                    res.append(i)
        return res

        

            

                
                



    

        
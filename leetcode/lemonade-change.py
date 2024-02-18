class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
    
        count_five,count_ten=0,0
        for i in range(len(bills)):
            if bills[i]==5:
                count_five+=1
               
            elif bills[i]==10:
                if count_five==0:
                    return False
                else:
                    count_five-=1
                    count_ten+=1
                    
                

            elif bills[i]==20 :
                if count_ten>0 and count_five>0:
                    count_ten-=1
                    count_five-=1
                   
                elif count_ten==0 and count_five>2:
                    
                    count_five-=3
                else:
                    return False
        return True

        
            
            
        
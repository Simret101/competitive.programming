class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target>= letters[-1]:
            return letters[0]
        else:
       
            x=bisect_right(letters,target) 
        
            return letters[x] 
            

        # l=0
        # r=len(letters)-1
        # while l<=r:

        #     mid=(l+r)//2
        #     if letters[mid]==target:
        #         if letters[mid+1]!=target:

        #             return letters[mid+1]
        #     elif letters[mid]>target:
        #         r=mid-1
        #     else :
        #         l=mid+1
        # else:
        #     return letters[0]
        
            
                
          
        

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """ 
       
        for i in range(len(board)):
            first_unique=set()
            for j in range(len(board[0])):
                if board[i][j]!="." and board[i][j] in first_unique :
                    return False
                else:
                    first_unique.add(board[i][j])

        for j in range(len(board[0])):
            second_unique=set()
            for i in range(len(board)):
                if board[i][j]!="." and board[i][j] in second_unique:
                    return False
                else:
                    second_unique.add(board[i][j])
        row=0
        col=0
        row1=0
        col1=0
        while row<3:
            col1=0
            col = 0
            while col<3:
                third_unique=set()
                for i in range(row1 , row1 +3):    
                    for j in range(col1, col1 +3):
                        if board[i][j]!="." and board[i][j] in third_unique:
                            return False
                        else:
                            third_unique.add(board[i][j])
                col1+=3
                col+= 1
            row += 1
            row1 += 3
        return True

                
                    
                
          
        
        
        

        
        
        
        
        
                    
        


     
      


        
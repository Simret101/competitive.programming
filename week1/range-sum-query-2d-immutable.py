class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows=len(matrix)
        cols=len(matrix[0])
        self.matrixes=[[0]*(cols+1) for i in range(rows+1)]
        for i in range(rows):
            prefix=0
            for j in range(cols):
                prefix+=matrix[i][j]
                above=self.matrixes[i][j+1]
                self.matrixes[i+1][j+1]=prefix+above
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,col1,row2,col2=row1+1,col1+1,row2+1,col2+1
        left=self.matrixes[row2][col1-1]
        above=self.matrixes[row1-1][col2]
        top_left=self.matrixes[row1-1][col1-1]
        bottom_right=self.matrixes[row2][col2]
        return bottom_right-above-left+top_left


   

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
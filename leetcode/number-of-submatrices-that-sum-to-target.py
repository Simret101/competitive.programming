class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        row = len(matrix)
        col = len(matrix[0])
        ans = 0
      
        for i in range(row):
            for j in range(1, col):
                matrix[i][j] += matrix[i][j-1]
          
        for k in range(col):
            for n in range(k, col):
                dict = {0: 1}
                tot = 0
                for i in range(row):
                    if k!=0:
                        prev_sum = matrix[i][k-1]
                    else:
                        prev_sum=0
                    curr_sum = matrix[i][n]-prev_sum
                    tot += curr_sum
                    if tot - target in dict:
                        ans += dict[tot - target]
                    dict[tot] = dict.get(tot, 0) + 1
        return ans



               
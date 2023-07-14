class Solution:
    def transpose(self, matrix, n):
        for row_ind in range(0,n):
            for col_ind in range(row_ind,n):
                temp = matrix[row_ind][col_ind]
                matrix[row_ind][col_ind] = matrix[col_ind][row_ind]
                matrix[col_ind][row_ind] = temp

mat = [[1, 1, 1, 1],
      [2, 2, 2, 2],
      [3, 3, 3, 3],
      [4, 4, 4, 4],]

Solution().transpose(mat,4)

print(mat)
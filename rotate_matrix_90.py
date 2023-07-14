class Solution:
    
    def row_inverter(self,a,n,max_row_ind):
        for row_ind in range(0,max_row_ind):
                    temp = a[row_ind][:]
                    a[row_ind][:] = a[n-row_ind-1][:]
                    a[n-row_ind-1][:] = temp
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self,a, n):
        for row_ind in range(0,n):
            for col_ind in range(row_ind,n):
                temp = a[row_ind][col_ind]
                a[row_ind][col_ind] = a[col_ind][row_ind]
                a[col_ind][row_ind] = temp

       

        if n==2:
            temp = a[0][:]
            a[0][:] = a[1][:]
            a[1][:] = temp
        else:
            if n%2==0:
                max_row_ind = int(n/2) - 1 
                self.row_inverter(a,n,max_row_ind+1)
            else:
                max_row_ind = int((n-1)/2)
                self.row_inverter(a,n,max_row_ind)

        

mat = [[2,94,49,30,24,85],
       [55,57,41,67,77,32],
       [9,45,40,27,24,38],
       [39,19,83,30,42,34],
       [16,40,59,5,31,78],
       [7,74,87,22,46,25]]
    

Solution().rotateby90(mat,6)

print(mat)
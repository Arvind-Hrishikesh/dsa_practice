class Solution:
    def insert(self, alist, index, n):
        for ind in range(index+1,n):
            if alist[ind]<alist[index]:
                temp = alist[ind]
                alist[ind] = alist[index]
                alist[index] = temp
        return alist


        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        for ind in range(0,n):
            alist = self.insert(alist,ind,n)


arr = [4, 1, 3, 9, 7]
Solution().insertionSort(arr,5)

print(arr)
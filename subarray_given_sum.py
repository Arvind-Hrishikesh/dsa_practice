class Solution:
    def subArraySum(self,arr, n, s): 
        if n == 0:
           return -1
        elif n == 1 and type(arr) == int:
           if arr == s:
               return [1]
           else:
               return [-1]
        else:
            for ind,x in enumerate(arr):
               sum = x
               sub_array_count = 0
               while (ind+sub_array_count)<n:
                   if sum < s:
                       sub_array_count+=1
                       try:
                           sum += arr[ind+sub_array_count]
                       except IndexError:
                           break
                   elif sum > s:
                       break
                   elif sum == s:
                       return ind+1,ind+sub_array_count+1
            return [-1]
                      

print(Solution().subArraySum([142,112,54,69,148,45,63,158,38,60,124,142,130,179,117,36,191,43,89,107,41,143,65,49,47,6,91,130,171,151,7,102,194,149,30,24,85,155,157,41,167,177,132,109,145,40,27,124,138,139,119,83,130,142,34,116,40,59,105,131,178,107,74,187,22,146,125,73,71,30,178,174,98,113],74,165))
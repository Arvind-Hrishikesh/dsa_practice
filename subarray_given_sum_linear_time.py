class Solution:
    def subArraySum(self,arr, n, s): 
        if s == 0:
            return [-1]
        begin = 0
        end = 1
        sub_array = arr[0]
        while begin<=end and end <=n:
            if sub_array < s:
                try:
                    sub_array += arr[end]
                except:
                    pass
                end+=1
            elif sub_array > s:
                sub_array -= arr[begin]
                begin+=1
            else:
                return begin+1,end
        return [-1]         
        

print(Solution().subArraySum([1,2,3,4],4,0))
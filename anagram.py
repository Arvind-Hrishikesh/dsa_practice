class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        dict_a={}
        for char in a:
            if char in dict_a.keys():
                dict_a[char]+=1
            else:
                dict_a[char]=1
        
        dict_b={}
        for char in b:
            if char in dict_b.keys():
                dict_b[char]+=1
            else:
                dict_b[char]=1
        
        if dict_a == dict_b:
            return True
        else:
            return False

print(Solution().isAnagram("allergy","allergic"))
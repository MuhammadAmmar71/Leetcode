class Solution:

    def __init__(self):
        pass




    

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        outerlist={}

        for var in strs:
            
            word="".join(sorted(var))
            
            if word in outerlist:
                outerlist[word].append(var)
                

            else:
                outerlist[word]=[var]

        return outerlist






    
       

    
        

        

sol1=Solution()
groupAnagrams=sol1.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(groupAnagrams)


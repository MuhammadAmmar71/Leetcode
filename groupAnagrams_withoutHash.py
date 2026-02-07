class Solution:

    def __init__(self):
        pass

    def Sorting(self,strs:list[str])->list[str]:

        sorted_list=[]
        for var in strs:
            sorted_list.append(sorted(var))

        sorted_list.sort()

        return sorted_list


    

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        sorted_list=self.Sorting(strs)

        outerList=[]
        innerList=[]

        innerList.append(sorted_list[0])

        for i in range(1,len(sorted_list)):

            
            
            if sorted_list[i]==sorted_list[i-1]:

                innerList.append(sorted_list[i])
            

            else:
                outerList.append(innerList)
           
                innerList = [sorted_list[i]]
                
        outerList.append(innerList)
        return outerList
                


    
        

        

sol1=Solution()
groupAnagrams=sol1.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(groupAnagrams)


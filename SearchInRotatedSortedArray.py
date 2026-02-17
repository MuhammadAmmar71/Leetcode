import random
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        flag=False
        for i in range(len(nums)):
            if nums[i]==target:
                return i
                flag=True
                break
            
        if flag!=True:
            return -1
            
            
obj=Solution()

nums=[4,5,6,7,0,1,2]
sorted_nums=sorted(nums)
print(sorted_nums)
rot=random.randint(1,len(sorted_nums))
print(rot)
i=0
for i in range(rot):
    x=sorted_nums.pop(0)
    sorted_nums.append(x)

index=obj.search(sorted_nums, 0)
print(index)
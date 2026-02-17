class MinStack:

    def __init__(self):
        self.arr=[]
        
        
    def push(self, val: int) -> None:
        self.arr.append(val)

    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        x=self.arr[-1]
        return x
        
    def getMin(self) -> int:
        sorted_arr=sorted(self.arr)
      
        y=sorted_arr[0]
        return y
        
        
        
obj = MinStack()
obj.push(5)
obj.push(3)
obj.push(9)
obj.push(1)
obj.push(8)
obj.pop()
param_3 = obj.top()
print(param_3)
param_4 = obj.getMin()
print(param_4)
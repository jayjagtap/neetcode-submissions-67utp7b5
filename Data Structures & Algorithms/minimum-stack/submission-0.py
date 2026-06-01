class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        # Maintain min stack
        temp = []
        while self.min_stack and val > self.min_stack[-1]:
            temp.append(self.min_stack.pop())
        
        self.min_stack.append(val)
        while temp:
            self.min_stack.append(temp.pop())
        

    def pop(self) -> None:
        if self.stack:
            pop = self.stack.pop()
        
        temp = []
        while 1:
            if self.min_stack[-1] == pop:
                self.min_stack.pop()
                break
            else:
                temp.append(self.min_stack.pop())
        
        while temp:
            self.min_stack.append(temp.pop())
        else: 
            return None
        

    def top(self) -> int:
        return self.stack[-1] if self.stack else None
        

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None
        

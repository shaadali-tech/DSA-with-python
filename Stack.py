class Stack:
    def __init__(self):
        self.stack = []


    def length(self):
        return len(self.stack)
    

    def peek(self):
        if len(self.stack)==0:
            raise Exception ("Stack is Empty")
        else :
            return self.stack[0]
    
    def push(self,value):
        return self.stack.insert(0,value)
    
    def pop(self):
        if len(self.stack)==0:
            raise Exception ("Stack is Empty")
        else :
            return self.stack.pop(0)

stk=Stack()

stk.push(10)
stk.push(20)
print(stk.peek())
stk.push(30)
print(stk.pop())
print(stk.peek())
    

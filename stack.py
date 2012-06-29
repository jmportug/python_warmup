class stack():

    def __init__(self):
        self.stk = []

    def push(self, value):
        self.stk.append(value)

    def pop(self):
        temp = self.stk[-1]
        del self.stk[-1]
        return temp

    def peek(self):
        if(len(self.stk) < 1): return
        return self.stk[-1]

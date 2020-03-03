class Stack:

    def __init__(self):
        self.stack = []

    def push(self, el):
        self.stack.append(el)
        return self.stack

    def pop(self):
        self.stack.pop()
        return self.stack

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) < 1



'''stack = Stack()
stack.push("first")
print(stack.stack)
stack.push("second")
print(stack.stack)
stack.peek()
print([stack.peek()])
#print(stack.stack)
stack.pop()
print(stack.stack)
print(stack.is_empty())'''
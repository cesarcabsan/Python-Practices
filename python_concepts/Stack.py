class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop(0)

    def peek(self):
        lifo = len(self.items)-1
        return self.items(lifo)

    def size(self):
        return len(self.items)

stack = Stack()
print(stack.isEmpty())

for i in range(0, 5):
    stack.push(i)

print(stack.size())
print(stack.items)

###Stack made with list (simple but slow)
stack_list = []
stack_list.append(1)
stack_list.append(2)
stack_list.append(3)
print("Full stack: ", stack_list)
print(stack_list.pop())
print(stack_list.pop())
print(stack_list.pop())
print("Empty stack: ", stack_list)

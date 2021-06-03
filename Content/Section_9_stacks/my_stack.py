# This is my Stack class

class Stack:

    def __init__(self):
        self.stack = []

    #Empty Stack
    def is_empty(self):
        return self.stack == []

    #Push
    def push(self, data):

        self.stack.append(data)

    #Pop, LIFO (Last in First Out)
    def pop(self):

        if self.is_empty() == True:
            print("This Stack is empty")

        else:
            temp = self.stack[-1]
            del self.stack[-1]
            return temp

    #Peek
    def peek(self):
        if self.is_empty() == True:
            print("There nothing to peek")
        
        else:
            return self.stack[-1]

    # size, could also just make a size counter in the class as well
    def size(self):
        return len(self.stack)


s1 = Stack()

s1.pop()

s1.push("A")
s1.push("B")
s1.push("C")

print(s1.peek())

s1.pop()

print(s1.peek())

print(s1.size())

s1.pop()

print(s1.peek(), s1.size())
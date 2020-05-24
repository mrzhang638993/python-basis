# 实现标准的异常操作逻辑和代码实现逻辑
class StackException(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data


class Stack:
    def __init__(self, size):
        self.s = []
        self.size = size
        self.top = -1

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def isFull(self):
        if self.pop == self.size - 1:
            return True
        else:
            return False

    def push(self, x):
        if self.isFull():
            raise StackException('stackOverFlowException')
        else:
            self.s.append(x)
            self.top += 1

    def pop(self):
        if self.isEmpty():
            raise StackException('stack is empty')
        else:
            return self.s.pop(0)

    def topEle(self):
        if self.isEmpty():
            raise StackException('stack is empty')
        else:
            return self.s[0]

    def bootom(self):
        if self.isEmpty():
            raise StackException('stack is empty')
        else:
            return self.s[-1]


# 学习资源学习。
stack = Stack(10)
print(stack.isEmpty())
stack.push(3)
print(stack.topEle())
print(stack.bootom())
stack.push(4)
print(stack.topEle())
print(stack.bootom())
stack.pop()
print(stack.topEle())
print(stack.bootom())

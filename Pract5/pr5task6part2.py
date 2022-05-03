from hypothesis.stateful import Bundle, RuleBasedStateMachine, rule, precondition
from hypothesis import given, strategies as st

class Stack:
    def __init__(self, size):
        self.data = [0] * size
        self.sp = 0

    def push(self, x):
        self.data[self.sp] = x
        self.sp += 1

    def get_top(self):
        return self.data[self.sp - 1]

    def dup(self):
        self.push(self.get_top())

    def pop(self):
        x = self.get_top()
        self.sp -= 1
        return x

    def swap(self):
        y, x = self.pop(), self.pop()
        self.push(y)
        self.push(x)



class ModelStack(RuleBasedStateMachine):
    def __init__(self):
        super().__init__()
        self.data = []
        self.stack = Stack(100)

    @rule(x=st.integers())
    def push(self, x):
        self.stack.push(x)
        self.data.append(x)

    @rule()
    @precondition(lambda self: len(self.data))
    def dup(self):
        self.stack.dup()
        self.data.append(self.data[-1])

    @rule()
    @precondition(lambda self: len(self.data))
    def pop(self):
        self.stack.pop()
        return self.data.pop()

    @rule()
    @precondition(lambda self: len(self.data) > 1)
    def swap(self):
        self.stack.swap()
        self.data[-1], self.data[-2] = self.data[-2], self.data[-1]

    @rule()
    def check_stacks(self):
        assert self.stack.data[:self.stack.sp] == self.data


test_stack = ModelStack.TestCase
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
    def push(self, val: int) -> None:
        if not self.stack:
            self.min.append(val)
        self.min.append(min(val, self.min[-1]))
        print('minimum: ', self.getMin())
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]

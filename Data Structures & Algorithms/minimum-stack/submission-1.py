class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
    def push(self, val: int) -> None:
        if not self.stack:
            self.min.append(val)
        elif val <= self.min[-1]:
            self.min.append(val)
        print('minimum: ', self.getMin())
        self.stack.append(val)

    def pop(self) -> None:
        s = self.stack.pop()
        val = self.min[-1]
        if s == val:
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]

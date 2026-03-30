class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        operation_stack = []

        for i in tokens:
            if i not in operators:
                operation_stack.append(int(i))
            else:
                a,b = int(operation_stack.pop()), int(operation_stack.pop())

                if i == "+":
                    operation_stack.append(a+b)
                elif i == '-':
                    operation_stack.append(b-a)
                elif i == '*':
                    operation_stack.append(a*b)
                else:
                    operation_stack.append(int(b/a))
        return operation_stack[0]
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                pop = ''
                if stack:
                    pop = stack.pop()
                if i == ')' and pop != '(':
                    return False
                elif i == ']' and pop != '[':
                    return False
                elif i == '}' and pop != '{':
                    return False
        if not stack:
            return True
        else:
            return False

        
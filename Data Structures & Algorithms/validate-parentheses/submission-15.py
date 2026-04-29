class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closingToOpen = {
          '}': '{',
          ']' : '[',
          ')': '('
        }
        for i in s:
          if i in closingToOpen:
            if stack and stack[-1] == closingToOpen[i]:
              stack.pop()
            else:
              return False
          else:
            stack.append(i)
        if not stack:
          return True
        else:
          return False
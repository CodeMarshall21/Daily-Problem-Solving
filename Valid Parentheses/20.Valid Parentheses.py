class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) < 2:
            return False
        for i in range(len(s)):
            if s[i] == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(s[i])
            elif s[i] == '}':
                if stack and  stack[-1] == "{":
                    stack.pop()
                else:
                    stack.append(s[i])
            elif s[i] == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        if (not stack):
            return True
        else:
            return False
            

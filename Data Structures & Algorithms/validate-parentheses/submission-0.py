class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            print(s[i], stack)
            if s[i] in "[{(":
                stack.append(s[i])
            elif not stack:
                return False
            elif s[i] == '}' and stack[-1] != '{':
                return False
            elif s[i] == ']' and stack[-1] != '[':
                return False 
            elif s[i] == ')' and stack[-1] != '(':
                return False
            
            elif not stack:
                return False
            else:
                stack.pop()
        if stack:
            return False
        return True
        
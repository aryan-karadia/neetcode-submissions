class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            elif c in ")]}":
                if len(stack) == 0:
                    return False
                last = stack[-1]
                if (last == '(' and c != ')' ) or (last == '{' and c != '}') or (last == '[' and c != ']'):
                    return False
                stack.pop()
        
        return len(stack) == 0
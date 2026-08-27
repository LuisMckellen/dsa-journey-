class Solution(object):
    def isValid(self, s):
        mapping={'(':')','[':']','{':'}'}
        stack=[]
        for c in s:
            if c in mapping:
                stack.append(c)
            else:
                if not stack or mapping[stack[-1]]!= c:
                    return False
                stack.pop()
        return not stack 

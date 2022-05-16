class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        for char in path:
            if char == '.' or char == "":
                continue
            elif char == '..':
                if stack:
                    stack.pop()
            else:
                stack.append("/" + char)

        if not stack:
            return '/'
        return ''.join(stack)

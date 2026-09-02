class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            # if token is an int, push on to stack

            if token == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)

            elif token == "-":
                b = stack.pop()
                a = stack.pop()

                stack.append(a - b)
            
            elif token == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)

            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))

            else:
                val = int(token)
                stack.append(val)

        return stack[0]

            

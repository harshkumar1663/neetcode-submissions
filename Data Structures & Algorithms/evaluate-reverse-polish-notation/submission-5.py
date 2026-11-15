class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i.lstrip("-").isnumeric():
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()

                if i == "+":
                    c = a + b
                elif i == "-":
                    c = a - b
                elif i == "*":
                    c = a * b
                elif i == "/":
                    c = int(a / b)

                stack.append(c)

        return stack[0]
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                # Pop the top two elements. 
                # 'b' is popped first, making it the right-side operand.
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # int(a / b) safely truncates toward zero in Python
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
                
        # The final result is the only remaining item in the stack
        return stack[0]
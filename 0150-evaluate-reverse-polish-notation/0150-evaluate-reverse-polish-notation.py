class Solution:
    # Define the class `Solution` which contains the method to evaluate an RPN expression.
    
    def evalRPN(self, tokens: List[str]) -> int:
        # Method to evaluate the Reverse Polish Notation (RPN) expression represented by `tokens`.
        # It uses a stack-based approach to compute the result.
        
        st = []
        # Initialize an empty stack `st` to store intermediate results.
        
        for c in tokens:
            # Iterate through each token in the input `tokens` list.
            
            if c == "+":
                # If the token is "+", pop the top two elements from the stack, add them, and push the result back.
                st.append(st.pop() + st.pop())
            
            elif c == "-":
                # If the token is "-", pop the top two elements, subtract the second popped element from the first, and push the result back.
                second, first = st.pop(), st.pop()
                st.append(first - second)
            
            elif c == "*":
                # If the token is "*", pop the top two elements, multiply them, and push the result back.
                st.append(st.pop() * st.pop())
            
            elif c == "/":
                # If the token is "/", pop the top two elements, divide the first popped element by the second, and push the integer result back.
                second, first = st.pop(), st.pop()
                st.append(int(first / second))
            
            else:
                # If the token is a number, convert it to an integer and push it onto the stack.
                st.append(int(c))
        
        return st[0]
        # After processing all tokens, the final result will be the only element left in the stack. Return it.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        op = ["*", "/", "+", "-"]
        stack = []

        for val in tokens:
            
            if val in op:
                num2 = stack.pop()
                num1 = stack.pop()
                print(f"{num1} , {num2} , {val}")
                match val:
                    case "*":
                        stack.append(num1*num2)
                    case "+":
                        stack.append(num1+num2)
                    case "-":
                        stack.append(num1-num2)
                    case "/":
                        stack.append(int(num1/num2))
            else:
                stack.append(int(val))
        
        return stack[0]




        
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        arr=["+","-","*","/"]
        sum=0
        for c in tokens:
            if c not in arr:
                stack.append(int(c))
            elif c == "+":
                
                sum=stack.pop(-2) + stack.pop(-1)
                
                stack.append(sum)
            elif c == "*":
                sum=stack.pop(-2) * stack.pop(-1)
                
                stack.append(sum)
            elif c == "-":
                sum=stack.pop(-2) - stack.pop(-1)
                
                stack.append(sum)
            elif c == "/":
                sum=int(stack.pop(-2) / stack.pop(-1))
                
                stack.append(sum)
        return stack.pop()
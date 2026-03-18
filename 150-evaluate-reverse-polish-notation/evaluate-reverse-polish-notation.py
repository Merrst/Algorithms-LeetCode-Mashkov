class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for t in tokens:
            if t in "+-*/":
                # Извлекаем два последних числа (второе операнд b, первое a)
                b, a = stack.pop(), stack.pop()
                if t == "+": stack.append(a + b)
                elif t == "-": stack.append(a - b)
                elif t == "*": stack.append(a * b)
                # В Python деление отрицательных чисел работает иначе, 
                # поэтому используем int(a / b) для округления к нулю
                elif t == "/": stack.append(int(a / b))
            else:
                # Если это число, просто кладем его в стек
                stack.append(int(t))
                
        return stack[0]
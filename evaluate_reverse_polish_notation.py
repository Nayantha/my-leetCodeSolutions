# https://leetcode.com/problems/evaluate-reverse-polish-notation/
def eval_rpn(tokens: list[str]) -> int:
    number_stack: list[int] = []
    for token in tokens:
        if token == "+":
            number_stack.append(number_stack.pop() + number_stack.pop())
        elif token == "-":
            num1, num2 = number_stack.pop(), number_stack.pop()
            number_stack.append(num2 - num1)
        elif token == "*":
            number_stack.append(number_stack.pop() * number_stack.pop())
        elif token == "/":
            num1, num2 = number_stack.pop(), number_stack.pop()
            number_stack.append(int(num2 / num1))
        else:
            number_stack.append(int(token))
    return number_stack[0]

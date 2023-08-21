# https://leetcode.com/problems/evaluate-reverse-polish-notation/
def eval_rpn(tokens: list[str]) -> int:
    number_stack: list[int] = []
    for token in tokens:
        if token.lstrip("-").isnumeric():
            number_stack.append(int(token))
            continue
        num1 = number_stack.pop()
        num2 = number_stack.pop()
        if token == "+":
            number_stack.append(num2 + num1)
        elif token == "-":
            number_stack.append(num2 - num1)
        elif token == "*":
            number_stack.append(num1 * num2)
        elif token == "/":
            number_stack.append(int(num2 / num1))
    return number_stack.pop()

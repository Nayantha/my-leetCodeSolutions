# https://leetcode.com/problems/evaluate-reverse-polish-notation/
def eval_rpn(tokens: list[str]) -> int:
    number_stack: list[int] = []
    for token in tokens:
        if token.isnumeric():
            number_stack.append(int(token))
    return number_stack.pop()

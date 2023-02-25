from stack import Stack
from decimal import Decimal


def main():
    rpn_stack = Stack()
    expression = input("Expression: ")
    expression = expression.strip().split(sep=" ")
    expression = [x for x in expression if x]

    for x in expression:
        if x == "+":
            n1 = Decimal(rpn_stack.pop())
            n2 = Decimal(rpn_stack.pop())
            n3 = n2 + n1
            rpn_stack.push(n3)
        elif x == "-":
            n1 = Decimal(rpn_stack.pop())
            n2 = Decimal(rpn_stack.pop())
            n3 = n2 - n1
            rpn_stack.push(n3)
        else:
            rpn_stack.push(x)

    print(f"{rpn_stack.pop()}")


if __name__ == "__main__":
    main()

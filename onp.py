def RNP(expr):
    length= len(expr)
    stack =[]
    for i in range(length):
        if (expr[i].isalpha()):
            print(expr[i],end="",flush=True)
        elif (expr[i] == ')'):
            print(stack[-1],end='',flush=True)
            stack.pop()
        elif (expr[i] != '('):
            stack.append(expr[i])

    return 0

t=input()
for i in range(int(t)):
    expr=input()
    RNP(expr)
    print()

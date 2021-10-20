def is_symmentrical(string):
    string = list(string)
    stack = ['asd']
    for i in range(len(string)):
        if string[i] != stack[-1]:
            stack.append(string[i])
        else:
            stack.pop()
    if stack[0] == 'asd' and len(stack) == 1:
        return True
    else:
        return False


print(is_symmentrical('1234213213213213213'))
variables = [0, 0, 0, 0]
registers = {'w': 0, 'x': 1, 'y': 2, 'z': 3}

linecount = 0
commands = []
for line in open('input.txt').readlines():
    linecount += 1
    com = line.strip().split()
    commands.append(com)

input_number = [9]*14


def operate(command, input_digit):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    op = com[0]
    a = registers[com[1]]
    if len(com) > 2:
        if com[2] in registers.keys():
            b = variables[registers[com[2]]]
        else:
            b = int(com[2])
    input_register = a
    if op == 'inp':
        variables[input_register] = alphabet[0]
        alphabet = alphabet[1:]
        variables[input_register] = input_digit

    elif op == 'add':
        if type(variables[a]) == int and type(b) == int:
            variables[input_register] = variables[a] + b
        elif b == 0:
            variables[input_register] = variables[input_register]
        elif variables[a] == 0:
            variables[input_register] = b
        else:
            variables[input_register] = '(' + \
                str(variables[a]) + "+" + str(b)+')'
    elif op == 'mul':
        if type(variables[a]) == int and type(b) == int:
            variables[a] = variables[a] * b
        elif variables[a] == 0 or b == 0:
            variables[input_register] = 0
        elif b == 1:
            pass
        else:
            variables[input_register] = '(' + \
                str(variables[a]) + '*' + str(b)+')'
    elif op == 'div':
        if type(variables[a]) == int and type(b) == int:
            variables[input_register] = int(variables[a] / b)
        elif b == 1:
            pass
        else:
            variables[input_register] = '(' + \
                str(variables[a]) + '/' + str(b)+')'
    elif op == 'mod':
        if type(variables[a]) == int and type(b) == int:
            variables[input_register] = variables[a] % b
        else:
            variables[input_register] = '(' + \
                str(variables[a]) + '%' + str(b)+')'
    elif op == 'eql':
        if type(variables[a]) == int and type(b) == int:
            variables[input_register] = int(variables[a] == b)
        elif type(b) is int and type(variables[a]) is str:
            if b >= 10 and len(variables[a]) == 1:
                variables[input_register] = 0
            else:
                variables[input_register] = '(' + \
                    str(variables[a]) + '=' + str(b)+')'
        else:
            variables[input_register] = '(' + \
                str(variables[a]) + '=' + str(b)+')'

    # print(linecount, variables)
for digit in range(10):
    for z in range(26):
        variables = [0, 0, 0, z]
        for com in commands[252-18:252]:
            operate(com, digit)
        if variables[3] == 0:
            print(digit, z, variables)
print(variables)

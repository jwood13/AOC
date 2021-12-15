
opens = '([{<'
closes = ')]}>'
close_map = {')': '(',
             '}': '{',
             ']': '[',
             '>': '<'}
penalty = {')': 3,
           '}': 57,
           ']': 1197,
           '>': 25137}
total_penalty = 0
for line in open('input.txt').readlines():
    buffer = []
    for char in line.strip():
        if char in opens:
            buffer.append(char)
        else:
            popped = buffer.pop()
            if popped != close_map[char]:
                print('error:'+char+popped)
                total_penalty += penalty[char]
                break
print(total_penalty)

# >340683

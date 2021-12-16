
opens = '([{<'
closes = ')]}>'
close_map = {')': '(',
             '}': '{',
             ']': '[',
             '>': '<'}
penalty = {')': 3,
           ']': 57,
           '}': 1197,
           '>': 25137}

auto_penalty = {'(': 1,
           '[': 2,
           '{': 3,
           '<': 4}

total_penalty = 0
line_penalties = []
for line in open('input.txt').readlines():
    buffer = []
    for char in line.strip():
        corrupted = False
        if char in opens:
            buffer.append(char)
        else:
            popped = buffer.pop()
            if popped != close_map[char]:
                print('error:'+char+popped)
                total_penalty += penalty[char]
                corrupted = True
                break
    if not corrupted:
        line_penalty = 0
        while len(buffer) > 0:
            line_penalty = line_penalty * 5 + auto_penalty[buffer.pop()]
        line_penalties.append(line_penalty)
line_penalties.sort()
print(line_penalties)
print(line_penalties[int(len(line_penalties)/2)])
print(total_penalty)

# >340683

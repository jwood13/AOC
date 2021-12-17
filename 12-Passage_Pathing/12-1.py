from collections import defaultdict
accessible = defaultdict(list)
for line in open("input.txt").readlines():
    a, b = line.strip().split('-')
    accessible[a].append(b)
    accessible[b].append(a)
print(accessible)
paths = ['start']
complete_paths = []
while len(paths) != 0:
    new_paths = []
    for path in paths:
        tail = path.split('-')[-1]
        for addition in accessible[tail]:
            if addition == 'end':
                complete_paths.append(path+'-'+addition)
            elif addition not in path or addition.upper() == addition:
                new_paths.append(path+'-'+addition)
    paths = new_paths
print(complete_paths)
print(len(complete_paths))

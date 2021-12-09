import numpy as np
init = True
count = 0
rows = 1000
cols = 12
bit_count = cols
storage = np.zeros((rows,cols),dtype=int)
for line in open("input.txt").readlines():
    if init:
        bit_count = len(line.strip())
        counter = np.zeros(bit_count,dtype=int)
        init = False
    bits = np.array([*line.strip()],dtype=bool)
    storage[count,:] = [int(x) for x in [*line.strip()]]
    counter += bits
    count += 1
o2binary = storage.copy()
co2binary = storage.copy()

# calculate o2 number
for col in range(cols):
    length = o2binary.shape[0]
    col_sum = np.sum(o2binary[:,col])
    if col_sum >= length/2:
        o2binary = o2binary[o2binary[:,col] == 1]
    else:
        o2binary = o2binary[o2binary[:,col] != 1]
    length = o2binary.shape[0]
    print(length)
    if length == 1:
        print(o2binary)
        o2 = sum(o2binary[0,i]*2**(bit_count - i - 1) for i in range(bit_count))
        break

for col in range(cols):
    length = co2binary.shape[0]
    col_sum = np.sum(co2binary[:,col])
    if col_sum >= length/2:
        co2binary = co2binary[co2binary[:,col] == 0]
    else:
        co2binary = co2binary[co2binary[:,col] != 0]
    length = co2binary.shape[0]
    print(length)
    if length == 1:
        print(co2binary)
        co2 = sum(co2binary[0,i]*2**(bit_count - i - 1) for i in range(bit_count))
        break


print(o2,co2,co2*o2)
# for i in range(bit_count)
# binary_gamma = [int(2*x/count) for x in counter]
# gamma = sum(binary_gamma[i]*2**(bit_count - i - 1) for i in range(bit_count))
# print(binary_gamma,gamma)
# epsilon = -sum((binary_gamma[i]-1)*2**(bit_count - i - 1) for i in range(bit_count))
# print(epsilon, epsilon * gamma)

# < 4038200
#   1071734
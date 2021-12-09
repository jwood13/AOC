import numpy as np
init = True
count = 0
for line in open("input.txt").readlines():
    if init:
        bit_count = len(line.strip())
        counter = np.zeros(bit_count,dtype=int)
        init = False
    bits = np.array([*line.strip()],dtype=int)
    counter += bits
    count += 1
binary_gamma = [int(2*x/count) for x in counter]
gamma = sum(binary_gamma[i]*2**(bit_count - i - 1) for i in range(bit_count))
print(binary_gamma,gamma)
epsilon = -sum((binary_gamma[i]-1)*2**(bit_count - i - 1) for i in range(bit_count))
print(epsilon, epsilon * gamma)

# < 4038200
#   1071734
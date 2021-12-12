import numpy as np
age_list = np.zeros(9)
with open("input.txt") as file:
    line = file.readline()
    for age in line.strip().split(','):
        age_list[int(age)] +=1

for day in range(256):
    births = age_list[0]
    for i in range(8):
        age_list[i] = age_list[i+1]
    age_list[8] = births
    age_list[6] += births
print(np.sum(age_list))
print(age_list)

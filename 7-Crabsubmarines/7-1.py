import numpy as np

crab_list = np.zeros(9)
with open("input.txt") as file:
    line = file.readline()
    crab_list = np.array([int(x) for x in line.strip().split(',')])

# Naive scan through all numbers
lowest_crab = crab_list.min()
highest_crab = crab_list.max()
print(lowest_crab,highest_crab)
smallest_fuel = highest_crab*len(crab_list)
for position in range(lowest_crab,highest_crab):
    fuel_cost = np.absolute(crab_list - position).sum()
    print(fuel_cost)
    if fuel_cost < smallest_fuel:
        smallest_fuel = fuel_cost
        ideal_position = position
print(smallest_fuel, ideal_position)
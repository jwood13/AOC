import numpy as np

crab_list = np.zeros(9)
with open("input.txt") as file:
    line = file.readline()
    crab_list = np.array([int(x) for x in line.strip().split(',')])

def fuel_step_cost(steps):
    if steps > 0:
        return steps + fuel_step_cost(steps-1)
    else:
        return steps

# Step cost is now (n**2+n)/2

# Naive scan through all numbers
lowest_crab = crab_list.min()
highest_crab = crab_list.max()
smallest_fuel = highest_crab**2*len(crab_list)
for position in range(lowest_crab,highest_crab):
    steps = np.absolute(crab_list - position)
    step_costs = (steps*steps).sum() + steps.sum()
    if step_costs < smallest_fuel:
        smallest_fuel = step_costs
        ideal_position = position
print(smallest_fuel/2, ideal_position)

## Wrong answer 199576870
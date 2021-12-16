from collections import defaultdict


def do_polymerisation(pair_list, insertions):
    new_polymer = pair_list.copy()
    # remove any pairs that will be inserted into
    for pos in insertions.keys():
        new_polymer[pos] = 0
    # Do the insertions
    for pos, val in insertions.items():
        insertion_sites = pair_list[pos]
        new_polymer[pos[0]+val] += insertion_sites
        new_polymer[val+pos[1]] += insertion_sites
    return new_polymer


def count_atoms(chain):
    atom_count = defaultdict(int)
    for pos, count in chain.items():
        atom_count[pos[0]] += count
    return atom_count


file = open('input.txt')
initial_string = file.readline()

file.readline()  # The blank line
insertions = {}
for line in file.readlines():
    position, insertion = line.strip().split(' -> ')
    insertions[position] = insertion

# Build the initial data structure from the starting string
pair_list = defaultdict(int)
for i in range(len(initial_string)-1):
    pair_list[initial_string[i]+initial_string[i+1]] += 1

# Do Loop the Polymerisation
for i in range(40):
    pair_list = do_polymerisation(pair_list, insertions)

atoms = count_atoms(pair_list)
print(atoms, sum(atoms.values()))
print(max(atoms.values())-min(atoms.values()))

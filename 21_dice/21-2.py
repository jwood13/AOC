from collections import defaultdict


def to_universe_notation(p1, p2, score1, score2):
    return f'{p1},{p2},{score1},{score2}'


def from_universe_notation(string):
    return [int(x) for x in string.split(',')]


def increment_universe(universe_string, player_number, generating_universes):
    p1, p2, s1, s2 = from_universe_notation(universe_string)
    places = [p1, p2]
    scores = [s1, s2]
    probability_distbn = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
    new_universes = {}
    for i in probability_distbn.keys():
        places = [p1, p2]
        places[player_number - 1] = (places[player_number - 1] + i) % 10
        scores = [s1, s2]
        scores[player_number - 1] += places[player_number - 1] + 1
        new_universes[to_universe_notation(
            *places, *scores)] = probability_distbn[i] * generating_universes
        # print(new_universes)
    return new_universes


def increment_multiverse(multiverse, player_number):
    next_multiverse = defaultdict(int)
    for universe_id, universe_count in multiverse.items():
        added_multiverses = increment_universe(
            universe_id, player_number, universe_count)
        for new_id, new_count in added_multiverses.items():
            next_multiverse[new_id] += new_count
    return next_multiverse


# sample
p1_start = 4
p2_start = 8
# true
p1_start = 3
p2_start = 7

p1 = p1_start - 1  # because of 0 indexing
p2 = p2_start - 1
p1_winners = 0
p2_winners = 0
multiverse = {to_universe_notation(p1, p2, 0, 0): 1}
loops = 1
while len(multiverse) > 0:
    loops += 1
    multiverse = increment_multiverse(multiverse, 1)
    universes_to_delete = []
    for universe_id, universe_count in multiverse.items():
        if from_universe_notation(universe_id)[2] >= 21:
            p1_winners += universe_count
            universes_to_delete.append(universe_id)
    for universe in universes_to_delete:
        multiverse.pop(universe)

    multiverse = increment_multiverse(multiverse, 2)
    universes_to_delete = []
    for universe_id, universe_count in multiverse.items():
        if from_universe_notation(universe_id)[3] >= 21:
            p2_winners += universe_count
            universes_to_delete.append(universe_id)
    for universe in universes_to_delete:
        multiverse.pop(universe)
print(p1_winners, p2_winners, loops, p1_winners > p2_winners)

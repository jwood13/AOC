from collections import defaultdict
import numpy as np

# list of all valid orientations
ROTATIONS = [np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
             np.array([[1, 0, 0], [0, -1, 0], [0, 0, -1]]),
             np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]]),
             np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]]),
             np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]]),
             np.array([[-1, 0, 0], [0, 1, 0], [0, 0, -1]]),
             np.array([[-1, 0, 0], [0, 0, 1], [0, 1, 0]]),
             np.array([[-1, 0, 0], [0, 0, -1], [0, -1, 0]]),
             np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]]),
             np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1]]),
             np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]]),
             np.array([[0, 1, 0], [0, 0, -1], [-1, 0, 0]]),
             np.array([[0, -1, 0], [-1, 0, 0], [0, 0, -1]]),
             np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]),
             np.array([[0, -1, 0], [0, 0, 1], [-1, 0, 0]]),
             np.array([[0, -1, 0], [0, 0, -1], [1, 0, 0]]),
             np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]]),
             np.array([[0, 0, 1], [0, -1, 0], [1, 0, 0]]),
             np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]]),
             np.array([[0, 0, 1], [-1, 0, 0], [0, -1, 0]]),
             np.array([[0, 0, -1], [0, -1, 0], [-1, 0, 0]]),
             np.array([[0, 0, -1], [0, 1, 0], [1, 0, 0]]),
             np.array([[0, 0, -1], [1, 0, 0], [0, -1, 0]]),
             np.array([[0, 0, -1], [-1, 0, 0], [0, 1, 0]]),
             ]


def rotation():
    def __init__(self):
        pass

    def apply(self, coord):
        return [x, y, z]


class Beacon():
    coords = [0, 0, 0]

    def __init__(self, coords):
        self.coords = np.array(coords, dtype=int)

    def __repr__(self):
        return str(self.coords)

    def add_neighbour(self, neighbour):
        displacement = neighbour.coords - self.coords
        distance_sq = np.dot(displacement, displacement)
        if distance_sq > 0:
            self.neighbours[distance_sq].append(displacement)

    def add_neighbours(self, neighbour_list):
        self.neighbours = defaultdict(list)
        for b in neighbour_list:
            self.add_neighbour(b)

    def signature_match(self, test_match):
        match_counter = 0
        matched_distances = []
        full_match = False
        for distance, pairs in self.neighbours.items():
            matches = min(len(self.neighbours[distance]),
                          len(test_match.neighbours[distance]))
            if matches > 0:
                matched_distances.append(distance)
            match_counter += matches
        if match_counter >= 11:
            for rotation in ROTATIONS:
                rotation_match = 0
                for dist in matched_distances:
                    for neighbour_a in self.neighbours[dist]:
                        for neighbour_b in test_match.neighbours[dist]:
                            rotated = np.matmul(rotation, neighbour_b)
                            if (neighbour_a == rotated).all():
                                rotation_match += 1
                if rotation_match >= 11:
                    full_match = True
                    break
            if full_match:
                sensor_displacement = self.coords - \
                    np.matmul(rotation, test_match.coords)
                return rotation, sensor_displacement
        return False


class Scanner():
    coords = np.array([0, 0, 0])
    orientation = ROTATIONS[0]
    beacons = []

    def __init__(self, beacon_list):
        self.beacons = []
        for item in beacon_list:
            coords = item.strip().split(',')
            self.beacons.append(Beacon(coords))
        for beacon in self.beacons:
            beacon.add_neighbours(self.beacons)

    def __repr__(self):
        return str(self.beacons[0]) +" "+str(self.coords)+' '+str(len(self.beacons))


def rotations(x, y, z):
    '''to retain chirality of the reference frame, any transformation needs to be 2 partial transformations i.e. 2 negations, or 1 rotation and 1 rotation'''
    negations = [
        [-x, y, z],
        [x, -y, z],
        [x, y, -z]]
    rotations = [
        [x, z, y],
        [y, x, z],
        [z, y, x]]


scanners = []
with open('sinput.txt') as file:
    beacons = []
    for line in file.readlines():
        if line.strip() == '':
            if len(beacons) > 0:
                new_scanner = Scanner(beacons)
                scanners.append(new_scanner)
            beacons = []
        elif line[: 3] == '---':
            pass
        else:
            beacons.append(line.strip())
    scanners.append(Scanner(beacons))
unlinked_scanners = scanners.copy()
scanners_to_remove = []
for scanner_a in scanners:
    for scanner in scanners_to_remove:
        unlinked_scanners.remove(scanner)
    scanners_to_remove = []
    if scanner_a in unlinked_scanners:
        unlinked_scanners.remove(scanner_a)
    
    for scanner_b in unlinked_scanners:
        result = False
        for beacon_a in scanner_a.beacons:
            for beacon_b in scanner_b.beacons:
                result = beacon_a.signature_match(beacon_b)
                if result:
                    break
            if result:
                break
        if result:
            scanners_to_remove.append(scanner_b)
            scanner_b.orientation = result[0]
            scanner_b.coords = np.matmul(scanner_a.orientation, result[1]) + scanner_a.coords
            print('link',scanner_a,scanner_b)
            # print('flag',scanner_b,scanner_a.coords)
            # print('scanner1 orientation', result[0], '\ndisplacement', result[1])
print(scanners)
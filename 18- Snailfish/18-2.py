import math
import json
import itertools


class snail_number():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.value = None
        self.send_left = None
        self.send_right = None
        if type(data) == list:
            self.left = snail_number(data[0])
            self.right = snail_number(data[1])
        elif type(data) == int:
            self.value = data
        elif type(data) == snail_number:
            self.value = data.value
            self.left = data.left
            self.right = data.right

    def __repr__(self):
        if self.value is not None:
            return str(self.value)
        else:
            return f"[{self.left},{self.right}]"

    def diag(self):
        print(self.left, self.right, self.value,
              self.send_left, self.send_right)

    def __add__(self, b):
        return snail_number([self, b]).reduce()

    def reduce_explode(self, depth=0):
        if self.value is None:
            if depth >= 4:
                self.send_left = self.left
                self.send_right = self.right
                self.right = None
                self.left = None
                self.value = 0
                return self
            else:
                self.left = self.left.reduce_explode(depth+1)
                self.send_left = self.left.send_left
                if self.left.send_right is not None:
                    self.right.dump_left(self.left.send_right)
                    self.left.reset_send_right()
                self.right = self.right.reduce_explode(depth+1)
                self.send_right = self.right.send_right
                if self.right.send_left is not None:
                    self.left.dump_right(self.right.send_left)
                    self.right.reset_send_left()
                return self
        else:
            return self

    def reduce_split(self):
        if self.value is not None:
            if self.value >= 10:
                return snail_number([int(self.value/2), math.ceil(self.value/2)])
            else:
                return self
        old_left = str(self.left)
        self.left = self.left.reduce_split()
        new_left = str(self.left)
        if old_left == new_left:
            self.right = self.right.reduce_split()
        return self

    def reduce(self):
        old = str(self)
        self.reduce_explode()
        new = str(self)
        while new != old:
            old = str(self)
            self.reduce_explode()
            new = str(self)
            if new == old:
                self.reduce_split()
                new = str(self)
        return self

    def dump_right(self, number):
        if self.value is not None:
            self.value += number.value
        else:
            self.right.dump_right(number)

    def dump_left(self, number):
        if self.value is not None:
            self.value += number.value
        else:
            self.left.dump_left(number)

    def reset_send_left(self):
        self.send_left = None
        if self.value is None:
            self.left.reset_send_left()

    def reset_send_right(self):
        self.send_right = None
        if self.value is None:
            self.right.reset_send_right()

    def magnitude(self):
        if self.value is None:
            return self.left.magnitude()*3 + self.right.magnitude()*2
        else:
            return self.value


def parse_string_to_list(string):
    return json.loads(string)


a = snail_number([1, 2])
b = snail_number([[1, 2], 3])
c = snail_number([9, [8, 7]])
d = snail_number([[1, 9], [8, 5]])
e = snail_number([[[[[9, 8], 1], 2], 3], 4])

# print(a+b)
# print(a)
# print(b)
# print(c)
# print(d, d.right)
# print(e.reduce())
# exploders = ([[[[[9,8],1],2],3],4],[7,[6,[5,[4,[3,2]]]]],[[6,[5,[4,[3,2]]]],1],[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]],[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]],[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]])
# for i in exploders:
#     print(snail_number(i).reduce())

a1 = snail_number([[[[4, 3], 4], 4], [7, [[8, 4], 9]]])
a2 = snail_number([1, 1])
# print((a1+a2),(a1+a2).reduce())
assert(str((a1+a2).reduce()) == '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')
assert(snail_number([[1, 2], [[3, 4], 5]]).magnitude() == 143)
assert(snail_number([[[[8, 7], [7, 7]], [[8, 6], [7, 7]]],
                     [[[0, 7], [6, 6]], [8, 7]]]).magnitude() == 3488)
# print('-----------------------------------------------')
# b1 = snail_number([[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]])
# b2 = snail_number([7,[[[3,7],[4,3]],[[6,3],[8,8]]]])
# b3 = snail_number([[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]])
# print("hi",(b1+b2).reduce())

# Read in numbers
numbers = []
with open('input.txt') as file:
    for line in file.readlines():
        numbers.append(parse_string_to_list(line))

highest_magnitude = 0
for combo in itertools.combinations(numbers, 2):
    a = snail_number(combo[0])
    a2 = snail_number(combo[0])
    b = snail_number(combo[1])
    b2 = snail_number(combo[1])
    c = a+b
    # c.diag()
    d = b2+a2
    # d.diag()
    results_list = (highest_magnitude, c.magnitude(), d.magnitude())
    highest_magnitude = max(results_list)
    print(results_list)

import math


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
        return snail_number([self, b])

    def reduce(self, depth=0):
        if depth >= 4 and self.value is None:
            print('deep')
            self.send_left = self.left
            self.send_right = self.right
            self.right = None
            self.left = None
            self.value = 0
            self.diag()
            print(self)
            return self
        if self.value is not None:
            if self.value >= 10:
                return snail_number([int(self.value/2), math.ceil(self.value/2)])
            else:
                return self
        else:
            self.left = self.left.reduce(depth+1)
            self.send_left = self.left.send_left
            self.right = self.right.reduce(depth+1)
            self.send_right = self.right.send_right
            self.diag()
            if self.right.send_left is not None:
                print('sl',self.send_left)
                self.left.dump_right(self.right.send_left)
            if self.left.send_right is not None:
                print('sr')
                self.right.dump_left(self.left.send_right)
            return self

    def dump_right(self, number):
        print('dr', number)
        if self.value is not None:
            self.value += number.value
        else:
            self.right.dump_right(number)

    def dump_left(self, number):
        print('dl', number)
        if self.value is not None:
            self.value += number.value
        else:
            self.left.dump_left(number)


a = snail_number([1, 2])
b = snail_number([[1, 2], 3])
c = snail_number([9, [8, 7]])
d = snail_number([[1, 9], [8, 5]])
e = snail_number([[[[[9, 8], 1], 2], 3], 4])

print(a+b)
print(a)
print(b)
print(c)
print(d, d.right)
print(e.reduce())

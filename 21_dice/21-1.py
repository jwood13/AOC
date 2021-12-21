
class Die():
    value = 0
    roll_count = 0

    def roll(self):
        self.value += 1
        if self.value > 100:
            self.value = 1
        self.roll_count += 1
        return self.value

    def roll3(self):
        sum = 0
        for i in range(3):
            sum += self.roll()
        return sum


# sample
p1_start = 4
p2_start = 8
# true
p1_start = 3
p2_start = 7

p1 = p1_start - 1  # because of 0 indexing
p1_score = 0
p2 = p2_start - 1
p2_score = 0
won = 0
die = Die()
while won == 0:
    p1 += die.roll3()
    p1 = p1 % 10
    p1_score += p1 + 1  # because of 0 indexing
    if p1_score >= 1000:
        won = 1
    else:
        p2 += die.roll3()
        p2 = p2 % 10
        p2_score += p2 + 1
        if p2_score >= 1000:
            won = 2
    print(p1, p2, p1_score, p2_score)
print(p1_score, p2_score, die.roll_count)
if won == 1:
    print(p2_score*die.roll_count)
else:
    print(p1_score*die.roll_count)

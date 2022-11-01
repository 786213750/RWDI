def findDH(courses):
    depth = 0
    horizontal = 0
    for d, a in courses:
        if d == "up":
            depth -= a

        elif d == "down":
            depth += a

        elif d == "forward":
            horizontal += a

        depth = max(0 , depth) #in case it try to go above water
    return depth * horizontal

course1 = [["forward", 5], ["down", 5], ["forward", 8], ["up", 3], ["down", 8], ["forward", 2]]
assert findDH(course1) == 150, "should be 150"

course2 = [["forward", 5]]
assert findDH(course2) == 0, "should be 0"

course3 = [["down", 5]]
assert findDH(course3) == 0, "should be 0"

course4 = [["forward", 5], ["up", 5], ["down", 8]]
assert findDH(course4) == 40, "test above water, should be 40"

#I store the input in a txt
with open('input_q2.txt', "r") as f:
    inputs = [[line.split()[0], int(line.split()[1])] for line in f]

print(findDH(inputs))


def findDHWithAim(courses):
    depth = 0
    horizontal = 0
    aim = 0
    for d, a in courses:
        if d == "up":
            aim -= a

        elif d == "down":
            aim += a

        elif d == "forward":
            horizontal += a
            depth += a * aim

    return depth * horizontal

assert findDHWithAim(course1) == 900, "should be 900"

assert findDHWithAim(course2) == 0, "should be 0"

assert findDHWithAim(course3) == 0, "should be 0"

course4 = [["forward", 5], ["down", 8]]
assert findDHWithAim(course4) == 0, "should be 0"

course5 = [["forward", 5], ["down", 8], ["up", 8], ["forward", 5]]
assert findDHWithAim(course5) == 0, "should be 0"

print(findDHWithAim(inputs))
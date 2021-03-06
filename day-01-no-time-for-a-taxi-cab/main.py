def parse_steps(filename):
    text_file = open(filename, "r")
    output = text_file.read().split(', ')
    return output


def move(d, a, f, p):
    if "L" in d:
        f -= 1
        if f == -1:
            f += 4
        if f == 4:
            f -= 4
    elif "R" in d:
        f += 1
        if f == -1:
            f += 4
        if f == 4:
            f -= 4
    if f == 0:
        p[1] +=a
    elif f == 1:
        p[0] += a
    elif f == 2:
        p[1] -= a
    elif f == 3:
        p[0] -= a
    return f


def how_far(position):
    distance = abs(position[0]) + abs(position[1])
    return distance


input = "directions.txt"

steps = parse_steps(input)
pointing = 0
pos = [0,0]

for step in steps:
    direction = step[0]
    amount = int(step[1:])
    pointing = move(direction, amount, pointing, pos)

distance  = how_far(pos)

print "Your position is %s, and Easter Bunny HQ is %s blocks away" %(pos,distance)





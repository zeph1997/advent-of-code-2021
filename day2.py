import getInput

input = getInput.get_input_for_day(2).split("\n")[:-1]

def part_one():
    horiz = 0
    depth = 0

    for i in input:
        direction, val = i.split(" ")
        if direction == "up":
            depth -= int(val)
        elif direction == "down":
            depth += int(val)
        else:
            horiz += int(val)

    out = horiz * depth
    print(out)

def part_two():
    horiz = 0
    depth = 0
    aim = 0

    for i in input:
        direction, val = i.split(" ")
        if direction == "up":
            aim -= int(val)
        elif direction == "down":
            aim += int(val)
        else:
            horiz += int(val)
            depth += int(val) * aim
    
    out = horiz * depth
    print(out)

part_one()
part_two()
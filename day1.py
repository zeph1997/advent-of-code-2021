import getInput

input = getInput.get_input_for_day(1).split("\n")[:-1]
input = list(map(int, input))

def part_one():
    count = 0
    for i in range(1,len(input)):
        if input[i] > input[i-1]:
            count += 1

    print(count)

def part_two():
    count = 0
    for i in range(3,len(input)):
        if sum(input[i-3:i]) < sum(input[i-2:i+1]):
            count += 1

    print(count)

part_one()
part_two()
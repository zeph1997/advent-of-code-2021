from AdventOfCodeInputReader import AdventOfCodeInputReader
import secret

reader = AdventOfCodeInputReader(secret.get_session_id(),2021,6)
input = reader.get_input()[0]
input = input.split(",")
input = list(map(int, input))
def part_one():
    for i in range(256):
        to_add = []
        for j in range(len(input)):
            if input[j] == 0:
                to_add.append(8)
                input[j] = 6
            else:
                input[j] -= 1
        input = input + to_add
        to_add = []

    print(len(input))
        
def part_two():
    fish_dict = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
    for i in input:
        fish_dict[i] += 1
    
    for i in range(256):
        to_add = fish_dict[0]
        for i in range(8):
            if i == 6:
                fish_dict[i] = fish_dict[i+1] + to_add
            else:
                fish_dict[i] = fish_dict[i+1]
        fish_dict[8] = to_add
    print(sum([y for x,y in fish_dict.items()]))

part_two()
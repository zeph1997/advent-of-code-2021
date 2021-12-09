from AdventOfCodeInputReader import AdventOfCodeInputReader
import secret
import math

reader = AdventOfCodeInputReader(secret.get_session_id(),2021,9)
input = reader.get_input()

for i in range(len(input)):
    input[i] = list(map(int,list(input[i])))

low_points = []

def is_low_point(i,j):
    top = input[i-1][j] if i != 0 else 10
    bottom = input[i+1][j] if i != len(input) - 1 else 10
    left = input[i][j-1] if j != 0 else 10
    right = input[i][j+1] if j != len(input[i]) - 1 else 10
    return input[i][j] < top and input[i][j] < bottom and input[i][j] < left and input[i][j] < right
        
def part_one():
    risk = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if is_low_point(i,j):
                risk += 1 + int(input[i][j])
                low_points.append((i,j))
    print(risk)

def is_low_point_basin(i,j):
    count = 1
    if i != 0:
        if input[i-1][j] > input[i][j] and input[i-1][j] != 9: # top
            count += is_low_point_basin(i-1,j)
    if i != len(input) - 1:
        if input[i+1][j] > input[i][j] and input[i+1][j] != 9: # bottom
            count += is_low_point_basin(i+1,j)
    if j != 0:
        if input[i][j-1] > input[i][j] and input[i][j-1] != 9: # left
            count += is_low_point_basin(i,j-1)
    if j != len(input[i]) - 1:
        if input[i][j+1] > input[i][j] and input[i][j+1] != 9: # right
            count += is_low_point_basin(i,j+1)
    input[i][j] = 9
    return count    

basins = []
def part_two():
    for i in low_points:
        basins.append(is_low_point_basin(i[0],i[1]))
    print(math.prod(sorted(basins,reverse=True)[:3]))

part_one()
part_two()
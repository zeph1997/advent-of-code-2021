from AdventOfCodeInputReader import AdventOfCodeInputReader
import secret


reader = AdventOfCodeInputReader(secret.get_session_id(),2021,11)
input = reader.get_input()

def flash(row,pos,):
    count = 1
    input[row][pos] = 0
    flashed[(row,pos)] = True
    for i in range(row-1,row+2):
        if i == -1 or i == len(input):
            continue
        else:
            for j in range(pos-1,pos+2):
                if j == -1 or  j == len(input[row]) or (i,j) in flashed:
                    continue
                else:
                    if input[i][j] >= 9:
                        count += flash(i,j)
                    else:
                        input[i][j] += 1
    return count

for i in range(len(input)):
    input[i] = list(map(int,list(input[i])))

sum_of_oct = len(input) * len(input[0])
flashes = 0
flashed = {}
for i in range(1000):
    flashed = {}
    for row in range(len(input)):
        for pos in range(len(input[row])):
            input[row][pos] += 1
    for row in range(len(input)):
        for pos in range(len(input[row])):
            if input[row][pos] > 9:
                flashes += flash(row,pos)
    if len(flashed) == sum_of_oct:
        print(i+1)
        break
print(flashes)
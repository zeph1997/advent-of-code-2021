from AdventOfCodeInputReader import AdventOfCodeInputReader
import secret

reader = AdventOfCodeInputReader(secret.get_session_id(),2021,13)
input = reader.get_input()

counter = 0
coords = []
while input[counter]:
    x,y = input[counter].split(",")
    coords.append((int(x),int(y)))
    counter += 1

fold = []
for i in input[counter+1:]:
    axis,num = i.split(" ")[-1].split("=")
    fold.append((axis,int(num)))

min_x = 1000
min_y = 1000
for i in fold:
    temp = {}
    if i[0] == "x":
        if i[1] < min_x:
            min_x = i[1]
        for j in coords:
            if j[0] > i[1]:
                temp[(j[0] - (j[0]-i[1])*2,j[1])] = 1
            else:
                temp[j] = 1
    else:
        if i[1] < min_y:
            min_y = i[1]
        for j in coords:
            if j[1] > i[1]:
                temp[(j[0],j[1] - (j[1]-i[1])*2)] = 1
            else:
                temp[j] = 1
    coords = []
    for i,j in temp.items():
        coords.append((i[0],i[1]))

draw = [["." for x in range(min_x)] for y in range(min_y) ]
for i,j in temp.items():
    draw[i[1]][i[0]] = "#"

final = []
for i in draw:
    final.append("".join(i))

for i in final:
    print(i)
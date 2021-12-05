from AdventOfCodeInputReader import AdventOfCodeInputReader
import secret

reader = AdventOfCodeInputReader(secret.get_session_id(),2021,5)
input = reader.get_input()

my_map = {}

for i in input:
    coord1,coord2 = i.split(" -> ")
    coords1 = coord1.split(",")
    coords1 = list(map(int, coords1))
    coords2 = coord2.split(",")
    coords2 = list(map(int, coords2))
    if coords1[0] == coords2[0] or coords1[1] == coords2[1]:
        if coords1[0] > coords2[0]:
            for x in range(coords2[0],coords1[0]+1):
                if (x,coords2[1]) in my_map:
                    my_map[(x,coords2[1])] += 1
                else:
                    my_map[(x,coords2[1])] = 1
        elif coords1[1] > coords2[1]:
            for y in range(coords2[1],coords1[1]+1):
                if (coords2[0],y) in my_map:
                    my_map[(coords2[0],y)] += 1
                else:
                    my_map[(coords2[0],y)] = 1
        elif coords1[0] < coords2[0]:
            for x in range(coords1[0],coords2[0]+1):
                if (x,coords1[1]) in my_map:
                    my_map[(x,coords1[1])] += 1
                else:
                    my_map[(x,coords1[1])] = 1
        elif coords1[1] < coords2[1]:
            for y in range(coords1[1],coords2[1]+1):
                if (coords1[0],y) in my_map:
                    my_map[(coords2[0],y)] += 1
                else:
                    my_map[(coords1[0],y)] = 1
        else:
            if (coords1[0],coords2[1]) in my_map:
                    my_map[(coords1[0],coords2[1])] += 1
            else:
                my_map[(coords1[0],coords2[1])] = 1
    elif abs(coords1[0] - coords2[0])/abs(coords1[1] - coords2[1]) == 1:       
        if coords1[0] < coords2[0]:
            if coords1[1] > coords2[1]: #downward slope
                diff_x = coords2[0] - coords1[0]
                diff_y = coords1[1] - coords2[1]
                if (coords1[0],coords1[1]) in my_map:
                    my_map[(coords1[0],coords1[1])] += 1
                else:
                    my_map[(coords1[0],coords1[1])] = 1
                for diff in range(max(diff_x,diff_y)):
                    if diff_x > 0:
                        diff_x -= 1
                    if diff_y > 0:
                        diff_y -= 1
                    if (coords2[0] - diff_x,coords2[1] + diff_y) in my_map:
                        my_map[(coords2[0] - diff_x,coords2[1] + diff_y)] += 1
                    else:
                        my_map[(coords2[0] - diff_x,coords2[1] + diff_y)] = 1
            elif coords1[1] < coords2[1]: #upward slope
                diff_x = coords2[0] - coords1[0]
                diff_y = coords2[1] - coords1[1]
                if (coords2[0],coords2[1]) in my_map:
                        my_map[(coords2[0],coords2[1])] += 1
                else:
                    my_map[(coords2[0],coords2[1])] = 1
                for diff in range(min(diff_x,diff_y)):
                    if diff_x > 0:
                        diff_x -= 1
                    if diff_y > 0:
                        diff_y -= 1
                    if (coords1[0] + diff_x,coords1[1] + diff_y) in my_map:
                        my_map[(coords1[0] + diff_x,coords1[1] + diff_y)] += 1
                    else:
                        my_map[(coords1[0] + diff_x,coords1[1] + diff_y)] = 1
        else:
            if coords1[1] < coords2[1]: #downward slope coord2 on left
                diff_x = coords1[0] - coords2[0]
                diff_y = coords2[1] - coords1[1]
                if (coords2[0],coords2[1]) in my_map:
                        my_map[(coords2[0],coords2[1])] += 1
                else:
                    my_map[(coords2[0],coords2[1])] = 1
                for diff in range(max(diff_x,diff_y)):
                    if diff_x > 0:
                        diff_x -= 1
                    if diff_y > 0:
                        diff_y -= 1
                    if (coords1[0] - diff_x,coords1[1] + diff_y) in my_map:
                        my_map[(coords1[0] - diff_x,coords1[1] + diff_y)] += 1
                    else:
                        my_map[(coords1[0] - diff_x,coords1[1] + diff_y)] = 1
            elif coords1[1] > coords2[1]: #upward slope
                diff_x = coords1[0] - coords2[0]
                diff_y = coords1[1] - coords2[1]
                if (coords1[0],coords1[1]) in my_map:
                    my_map[(coords1[0],coords1[1])] += 1
                else:
                    my_map[(coords1[0],coords1[1])] = 1
                for diff in range(max(diff_x,diff_y)):
                    if diff_x > 0:
                        diff_x -= 1
                    if diff_y > 0:
                        diff_y -= 1
                    if (coords2[0] + diff_x,coords2[1] + diff_y) in my_map:
                        my_map[(coords2[0] + diff_x,coords2[1] + diff_y)] += 1
                    else:
                        my_map[(coords2[0] + diff_x,coords2[1] + diff_y)] = 1

print(len([i for i,j in my_map.items() if j > 1]))

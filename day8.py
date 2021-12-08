from AdventOfCodeInputReader import AdventOfCodeInputReader
import secret

reader = AdventOfCodeInputReader(secret.get_session_id(),2021,8)
input = reader.get_input()

def part_one():
    counter = 0
    for i in input:
        front,back = i.split("|")
        items = back.split()
        for j in items:
            if len(j) == 2 or len(j) == 4 or len(j) == 3 or len(j) == 7:
                counter += 1
    print(counter)
#input = ["be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe","edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
# "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
# "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
# "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
# "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
# "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
# "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
# "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
# "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"]
print(len(input))
counter = 0
for i in input:
    front,back = i.split("|")
    front = front.split()
    map_dict = {}
    mapper_dict = {}
    two_three_five = []
    six_nine_zero = []
    for j in front:
        if len(j) == 2:
            map_dict["".join(sorted(list(j)))] = 1
            mapper_dict[1] ="".join(sorted(list(j)))
        elif len(j) == 3:
            map_dict["".join(sorted(list(j)))] = 7
            mapper_dict[7] ="".join(sorted(list(j)))
        elif len(j) == 4:
            map_dict["".join(sorted(list(j)))] = 4
            mapper_dict[4] ="".join(sorted(list(j)))
        elif len(j) == 7:
            map_dict["".join(sorted(list(j)))] = 8
            mapper_dict[8] ="".join(sorted(list(j)))
        else:
            two_three_five.append("".join(sorted(list(j)))) if len(j) == 5 else six_nine_zero.append("".join(sorted(list(j))))
            map_dict["".join(sorted(list(j)))] = 0
    four_neg = [x for x in mapper_dict[8] if x not in mapper_dict[4]]
    for j in two_three_five:
        # catch 2
        if (all(x in j for x in four_neg)):
            map_dict["".join(sorted(list(j)))] = 2
            mapper_dict[2] = "".join(sorted(list(j)))
            two_three_five.pop(two_three_five.index(j))
    if len([x for x in two_three_five[0] if x not in mapper_dict[2]]) == 1:
        map_dict["".join(sorted(list(two_three_five[0])))] = 3
        mapper_dict[3] = "".join(sorted(list(two_three_five[0])))
        map_dict["".join(sorted(list(two_three_five[1])))] = 5
        mapper_dict[5] = "".join(sorted(list(two_three_five[1])))
    else:
        map_dict["".join(sorted(list(two_three_five[1])))] = 3
        mapper_dict[3] = "".join(sorted(list(two_three_five[1])))
        map_dict["".join(sorted(list(two_three_five[0])))] = 5
        mapper_dict[5] = "".join(sorted(list(two_three_five[0])))

    for j in six_nine_zero:
        # catch 9
        if not (all(x in j for x in four_neg)):
            map_dict["".join(sorted(list(j)))] = 9
            mapper_dict[9] = "".join(sorted(list(j)))
            six_nine_zero.pop(six_nine_zero.index(j))
    if len([x for x in six_nine_zero[0] if x not in mapper_dict[5]]) == 1:
        map_dict["".join(sorted(list(six_nine_zero[0])))] = 6
        mapper_dict[6] = "".join(sorted(list(six_nine_zero[0])))
        map_dict["".join(sorted(list(six_nine_zero[1])))] = 0
        mapper_dict[0] = "".join(sorted(list(six_nine_zero[1])))
    else:
        map_dict["".join(sorted(list(six_nine_zero[1])))] = 6
        mapper_dict[6] = "".join(sorted(list(six_nine_zero[1])))
        map_dict["".join(sorted(list(six_nine_zero[0])))] = 0
        mapper_dict[0] = "".join(sorted(list(six_nine_zero[0])))
    
    items = back.split()
    out = []
    for j in items:
        out.append(str(map_dict["".join(sorted(list(j)))]))
    print(map_dict, out, items)
    #print(int("".join(out)))
    counter += int("".join(out))
    
print(counter)
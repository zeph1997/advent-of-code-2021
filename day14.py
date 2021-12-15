from AdventOfCodeInputReader import AdventOfCodeInputReader
import secret
from collections import defaultdict

reader = AdventOfCodeInputReader(secret.get_session_id(),2021,14)
input = reader.get_input()

template = input[0]
pairs = {}
for i in input[2:]:
    pair,add = i.split(" -> ")
    pairs[pair] = add

real_counter = defaultdict(int)
for i in range(1,len(template)):
    real_counter[template[i-1:i+1]] += 1

for i in range(40):
    temp_dict = defaultdict(int)
    for j in real_counter.keys():
        if j in pairs:
            temp_dict[j[0] + pairs[j]] += real_counter[j]
            temp_dict[pairs[j] + j[1]] += real_counter[j]
        else:
            temp_dict[j] += real_counter[j]
    real_counter = temp_dict

final_dict = {}
for i,j in real_counter.items():
    if i[0] in final_dict:
        final_dict[i[0]] += j
    else:
        final_dict[i[0]] = j
    if i[1] in final_dict:
        final_dict[i[1]] += j
    else:
        final_dict[i[1]] = j
final_dict[template[0]] += 1
final_dict[template[-1]] += 1
print((max(final_dict.values()) - min(final_dict.values()))//2)

    # temp = ""
    # for j in range(1,len(template)):
    #     temp += template[j-1]
    #     temp += pairs[template[j-1:j+1]]
    # temp += template[-1]
    # template = temp

# temp = list(template)
# counter_dict = defaultdict(int)
# for i in temp:
#     counter_dict[i] += 1
# min = 999999999999999
# lowest = ""

# for i,j in real_counter.items():
#     if j < min:
#         min = j
#         lowest = i

# print(real_counter)
# print(temp.count(max(set(temp), key = temp.count)) - temp.count(lowest))



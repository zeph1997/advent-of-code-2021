from AdventOfCodeInputReader import AdventOfCodeInputReader
import secret

reader = AdventOfCodeInputReader(secret.get_session_id(),2021,16)
input = reader.get_input()

mapper ={
    "0":"0000",
    "1":"0001",
    "2":"0010",
    "3":"0011",
    "4":"0100",
    "5":"0101",
    "6":"0110",
    "7":"0111",
    "8":"1000",
    "9":"1001",
    "A":"1010",
    "B":"1011",
    "C":"1100",
    "D":"1101",
    "E":"1110",
    "F":"1111",
}
print(input)
new_input = ""
for i in input[0]:
    new_input += mapper[i]

all_inputs = []

cursor = 0
ver_counter = 0
#new_input = "1101001011111110001010000011100000000000011011110100010100101001000100100000000011101110000000001101010000001100100000100011000001100000"
new_input = "1101001011111110001010001110111000000000110101000000110010000010001100000110000000111000000000000110111101000101001010010001001000000000"
print("max",len(new_input))
while cursor < len(new_input)-1:
    start = cursor
    ver = new_input[cursor:cursor+3]
    typeID = new_input[cursor+3:cursor+6]
    temp = 0
    for j in range(2,-1,-1):
        temp += int(ver[j]) * (2**(2-j))
    ver_counter += temp
    type_num = 0
    for j in range(2,-1,-1):
        type_num += int(int(typeID[j]) * (2**(2-j)))
    print("cursor:",cursor)
    print("ver num:",temp)
    print("ver:",ver)
    if type_num == 4:
        cursor = cursor + 6
        while cursor < len(new_input):
            if new_input[cursor] == "0":
                cursor += 5
                if (cursor - start) % 4 != 0:
                    cursor += 4 - (cursor%4)
                break
                # while new_input[cursor] == "0":
                #     cursor += 1
                #     if (cursor - start) % 4 == 0:
                #         break
            else:
                cursor = cursor + 5
        
        all_inputs.append(new_input[start:cursor])
        print()
    else:
        cursor = cursor + 6
        if new_input[cursor] == "1":
            cursor += 1
            num_of_sub = 0
            for k in range(10,-1,-1):
                num_of_sub += int(int(new_input[cursor+k]) * (2**(10-k)))
            print("num of sub",num_of_sub)
            jump = num_of_sub * 11
            print("jump",jump)
            print("new cursor",cursor)
            cursor += int(11 + (jump) + 1)
            print("add cursor alrd",cursor)
            # if new_input[cursor] == 0:
            #     while new_input[cursor] == 0:
            #         cursor += 1
            # all_inputs.append(new_input[start:cursor])
        else:
            cursor += 1
            len_of_sub = 0
            for k in range(14,-1,-1):
                len_of_sub +=  int(int(new_input[cursor+k]) * (2**(14-k)))
            
            cursor += int(15 + len_of_sub + 1)
        print("cursor check",cursor)
        print("start",start)
        if (cursor - start) % 4 != 0:
            cursor += 4 - ((cursor-start)%4)
            print("add cursor",cursor)
        # if new_input[int(cursor)] == "0":
        #     while new_input[int(cursor)] == "0":
        #         cursor += 1
        #         if (cursor - start) % 4 == 0:
        #             break
        
        all_inputs.append(new_input[start:cursor])
        print()
print("ver counter:",ver_counter)
print(len(all_inputs))
#new_input = ["110100101111111000101000","11101110000000001101010000001100100000100011000001100000","00111000000000000110111101000101001010010001001000000000"]
# ver_counter = 0
# for i in new_input:
#     temp = 0
#     for j in range(2,-1,-1):
#         temp += int(i[j]) * (2**(2-j))
#     ver_counter += temp

# print(ver_counter)
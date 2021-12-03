import getInput

input = getInput.get_input_for_day(3).split("\n")[:-1]

def part_one():
    char_length = len(input[0])
    counter = [0 for _ in range(char_length)]

    for i in input:
        for j in range(len(i)):
            counter[j] += int(i[j])

    gamma = [0 for _ in range(char_length)]
    epsilon = [0 for _ in range(char_length)]

    for i in range(len(counter)):
        if counter[i]/len(input) > 0.5:
            gamma[i] = '1'
            epsilon[i] = '0'
        else:
            gamma[i] = '0'
            epsilon[i] = '1'

    gamma_dec = int(''.join(gamma),2)
    epsilon_dec = int(''.join(epsilon),2)

    print(gamma_dec*epsilon_dec)

def part_two():
    char_length = len(input[0])
    oxygen = [0 for _ in range(char_length)]
    temp_input = input[::]
    for i in range(len(oxygen)):
        digit_sum = 0
        for j in temp_input:
            digit_sum += int(j[i])
        oxygen[i] = '1' if digit_sum/max(len(temp_input),1) >= 0.5 else '0'
        temp_input = [x for x in temp_input if list(x[:i+1]) == oxygen[:i+1]]
        if len(temp_input) == 1:
            oxygen = list(temp_input[0])
            break

    
    co_scrubber = [0 for _ in range(char_length)]
    temp_input = input[::]
    for i in range(len(co_scrubber)):
        digit_sum = 0
        for j in temp_input:
            digit_sum += int(j[i])
        co_scrubber[i] = '0' if digit_sum/max(len(temp_input),1) >= 0.5 else '1'
        
        temp_input = [x for x in temp_input if list(x[:i+1]) == co_scrubber[:i+1]]
        if len(temp_input) == 1:
            co_scrubber = list(temp_input[0])
            break
    
    oxygen_dec = int(''.join(oxygen),2)
    co_scrubber_dec = int(''.join(co_scrubber),2)

    print(oxygen_dec*co_scrubber_dec)

part_two()
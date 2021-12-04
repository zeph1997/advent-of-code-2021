from AdventOfCodeInputReader import AdventOfCodeInputReader
import secret

reader = AdventOfCodeInputReader(secret.get_session_id(),2021,4)
input = reader.get_input()

chosen_numbers = input[0].split(",")
bingo_sheets = []
temp_sheet = []
shadow_bingo_sheets = []
input = input[2:]
winning_sheet = []
last_num = 0
last_sheet = []

new_board = False
for i in input:
    if i == "":
        bingo_sheets.append(temp_sheet)
        temp_sheet = []
    else:
        temp_sheet.append(i.split())

def mark_sheets(bingo_sheets,num):
    for sheet in bingo_sheets:
        for row in sheet:
            if num in row:
                row[row.index(num)] = ""

def check_sheets(bingo_sheets):
    sheets = []
    for sheet in range(len(bingo_sheets)):
        # Check column first
        rows = len(bingo_sheets[sheet])
        for pos in range(rows):
            for row in range(rows):
                if bingo_sheets[sheet][row][pos] != "":
                    break
            else:
                return bingo_sheets[sheet]
        
        # Check rows
        for row in bingo_sheets[sheet]:
            if len("".join(row)) == 0:
                return bingo_sheets[sheet]
    return False

def check_sheets_two(bingo_sheets):
    sheets = []
    for sheet in range(len(bingo_sheets)):
        # Check column first
        rows = len(bingo_sheets[sheet])
        for pos in range(rows):
            for row in range(rows):
                if bingo_sheets[sheet][row][pos] != "":
                    break
            else:
                sheets.append(sheet)
        
        # Check rows
        for row in bingo_sheets[sheet]:
            if len("".join(row)) == 0:
                sheets.append(sheet)
    return sheets[::-1]

def part_one():
    for i in chosen_numbers:
        mark_sheets(bingo_sheets,i)
        winning_sheet = check_sheets(bingo_sheets)
        if winning_sheet:
            last_num = i
            break

    result = 0
    for i in range(len(winning_sheet)):
        for j in range(len(winning_sheet[i])):
            if winning_sheet[i][j] != "":
                result += int(winning_sheet[i][j])

    print(result * int(last_num))

def part_two():
    global last_sheet
    global last_num
    for i in chosen_numbers:
        mark_sheets(bingo_sheets,i)
        for winning_sheet in check_sheets_two(bingo_sheets):
            if len(bingo_sheets) == 1:
                last_sheet = bingo_sheets[0]
                last_num = i
                bingo_sheets.pop(winning_sheet)
                break
            else:
                bingo_sheets.pop(winning_sheet)
        if len(bingo_sheets) == 0:
            break
    
    result = 0
    for i in range(len(last_sheet)):
        for j in range(len(last_sheet[i])):
            if last_sheet[i][j] != "":
                result += int(last_sheet[i][j])

    print(result * int(last_num))

part_one()
part_two()
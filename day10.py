from AdventOfCodeInputReader import AdventOfCodeInputReader
import secret
import math

reader = AdventOfCodeInputReader(secret.get_session_id(),2021,10)
input = reader.get_input()

counter = 0
bad = {
    ")":3,
    "]":57,
    "}":1197,
    ">":25137
}
remove = []
for i in range(len(input)):
    checker = []
    for j in range(len(input[i])):
        if input[i][j] == "(" or input[i][j] == "[" or input[i][j] == "{" or input[i][j] == "<":
            checker.append(input[i][j])
        else:
            to_check = checker.pop()
            if (to_check == "(" and input[i][j] != ")") or (to_check == "[" and input[i][j] != "]") or (to_check == "{" and input[i][j] != "}") or (to_check == "<" and input[i][j] != ">"):
                counter += bad[input[i][j]]
                remove.append(i)
                break
print(counter)

complete = {
    ")":1,
    "]":2,
    "}":3,
    ">":4
}
flip = {
    "(":")",
    "[":"]",
    "{":"}",
    "<":">"
}

# for j in remove[::-1]:
#     input.pop(j)
scores = []
for i in range(len(input)):
    checker = []
    for j in range(len(input[i])):
        if input[i][j] == "(" or input[i][j] == "[" or input[i][j] == "{" or input[i][j] == "<":
            checker.append(input[i][j])
        else:
            to_check = checker.pop()
            if (to_check == "(" and input[i][j] != ")") or (to_check == "[" and input[i][j] != "]") or (to_check == "{" and input[i][j] != "}") or (to_check == "<" and input[i][j] != ">"):
                break
    else:
        score = 0
        for j in checker[::-1]:
            #score = score * 5 + complete[j]
            score = score * 5 + complete[flip[j]]
        scores.append(score)

print(sorted(scores)[len(scores)//2])



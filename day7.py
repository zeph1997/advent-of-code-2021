from AdventOfCodeInputReader import AdventOfCodeInputReader
import secret
import sys

reader = AdventOfCodeInputReader(secret.get_session_id(),2021,7)
input = reader.get_input()[0].split(",")
input = list(map(int,input))

fuel_used = sys.maxsize
loc = 0
for i in range(min(input),max(input)):
    fuel = sum([(abs(x-i)/2)*(2+(abs(x-i)-1)) for x in input])
    if fuel < fuel_used:
        loc = i
        fuel_used = fuel
print(loc)
print(fuel_used)
    

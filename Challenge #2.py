#Day 2: Rock Paper Scissors
# https://adventofcode.com/2022/day/2
# https://adventofcode.com/2022/day/2/input

FilePath = "C:\\Users\\James Mills\\Documents\\GitHub\\Advent-of-Code-2022\\inputs\\input 2.txt"

OpenFile = open(FilePath,"r")
data = OpenFile.readlines()                  #access data

#opponent hand types and point values
A = 1                   #Rock
B = 2                   #Paper
C = 3                   #Scissors

#player(you) hand types and point values
X = 1                   #Rock
Y = 2                   #Paper
Z = 3                   #Scissors

#scores for outcome types
win = 6
draw = 3
loose = 0

i = 0

for str in data:                     #for any indexed item line read from "data.txt" file
    
          


#run through each line in a for loop (will need for loop inside of a for loop)
#run through strings in the line to determine which of the above characters are being played
#calculate outcome for each line individually
#calculate sum total
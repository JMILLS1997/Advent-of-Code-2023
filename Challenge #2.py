#Day 2: Rock Paper Scissors
# https://adventofcode.com/2022/day/2
# https://adventofcode.com/2022/day/2/input

FilePath = "C:\\Users\\James Mills\\Documents\\GitHub\\Advent-of-Code-2022\\inputs\\input 2.txt"

OpenFile = open(FilePath,"r")
data = OpenFile.read()                  #access data

#points per type of hand played
A = 1                   #Rock
B = 2                   #Paper
C = 3                   #Scissors

#response hand types
X = 1                   #Rock
Y = 2                   #Paper
Z = 3                   #Scissors

#scores for outcome types
win = 6
draw = 3
loose = 0



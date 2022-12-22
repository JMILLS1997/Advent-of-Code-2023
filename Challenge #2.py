#Day 2: Rock Paper Scissors
# https://adventofcode.com/2022/day/2
# https://adventofcode.com/2022/day/2/input

FilePath = "C:\\Users\\James Mills\\Documents\\GitHub\\Advent-of-Code-2022\\inputs\\input 2.txt"

OpenFile = open(FilePath,"r")
data = OpenFile.readlines()                 #access data
adjData = [x[:-1] for x in data]            #removes rightmost character from list data for every instance in "data" list

#score dictionary
#A = X = 1               #Rock
#B = Y = 2               #Paper
#C = Z = 3               #Scissors
DictPlrHnd = {'X': 1, 'Y': 2, 'Z': 3}

#scores for outcome types
#win = 6
#draw = 3
#loose = 0
DictOC = {'A Z': 0, 'B X': 0, 'C Y': 0, 'A X': 3, 'B Y': 3, 'C Z': 3, 'A Y': 6, 'B Z': 6, 'C X': 6}

#player scores var
playerscr = []

for str in adjData:
    for key1, value1 in DictOC.items():
        if key1 == str:
            print(key1)
            for key2, value2 in DictPlrHnd.items():
                if key1[2] == key2:
                    print(key2)
            else:
                pass
            pass
        else:
            pass

#ADD values to list, do same thing for the DictPlr dict and add those values to a list.
#Will need to compare hand type to game outcome to determin which hand type occurs in the game outcome ('Y' found in 'A Y')
#simple character comparason for the two strings, one at str[0] and the other at str[2]
#Day 2: Rock Paper Scissors
# https://adventofcode.com/2022/day/2
# https://adventofcode.com/2022/day/2/input

FilePath = "C:\\Users\\James Mills\\Documents\\GitHub\\Advent-of-Code-2022\\inputs\\input 2.txt"

OpenFile = open(FilePath,"r")
data = OpenFile.readlines()                  #access data

#score dictionary
#A = X = 1               #Rock
#B = Y = 2               #Paper
#C = Z = 3               #Scissors
DictScr1 = {'A': 1, 'B': 2, 'C': 3}
DictScr2 = {'X': 1, 'Y': 2, 'Z': 3}

#scores for outcome types
#win = 6
#draw = 3
#loose = 0
DictWin = {'A Z': 6, 'B X': 6, 'C Y': 6}
DictDrw = {'A X': 3, 'B Y': 3, 'C Z': 3}
DictLse = {'A Y': 0, 'B Z': 0, 'C X': 0}

#player scores var
playerscr = 0
opponentscr = 0
gamescr = 0

for lines in data:
    for eachkey in DictWin.keys():
        if eachkey in lines:
            print('win')
        else:
            pass
    
    for eachkey in DictWin.keys():
            if eachkey in lines:
                print('draw')
            else:
                pass
    
    for eachkey in DictWin.keys():
            if eachkey in lines:
                print('loose')
            else:
                pass
    




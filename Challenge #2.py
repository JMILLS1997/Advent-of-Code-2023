#Day 2: Rock Paper Scissors
# https://adventofcode.com/2022/day/2
# https://adventofcode.com/2022/day/2/input

FilePath = "C:\\Users\\James Mills\\Documents\\GitHub\\Advent-of-Code-2022\\inputs\\input 2.txt"

OpenFile = open(FilePath,"r")
data = OpenFile.readlines()                 # access data, reads all lines in file
adjData = [x[:-1] for x in data]            # removes rightmost character from list data for every instance in "data" list

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
playerscr1 = []
playerscr2 = []

for str in adjData:                                             # for all instances(1) in list "adjData"...
    for key1, value1 in DictOC.items():                         # for all instances(2) in dict. "DictOC"...
        if key1 == str:                                         # if both instances listed above (1) and (2) match...
            playerscr1.append(value1)                            # append the list "playerscr" with the dict. value from "DictOC"
            for key2, value2 in DictPlrHnd.items():             # for all instances(3) in dict. "DictPlrHnd"...
                if key1[2] == key2:                             # if both instances (2) and (3) match...
                    playerscr1.append(value2)                    # append the list "playerscr" with dict. value from "DictPlrHnd"
            else:                                               # Pass if data does not match instance (2).
                pass
            pass
        else:
            pass

print(sum(playerscr1))                                           # sum of all items in list, print.

##################### PART TWO ##### 

#strategy guide
#A = X = 1               #Rock
#B = Y = 2               #Paper
#C = Z = 3               #Scissors
DictStrtgy = {'X': 0, 'Y': 3, 'Z': 6}                            # X = loose, Y = draw, Z = win
DictRevOC = {'A Z': 'Y', 'B X': 'X', 'C Y': 'Z', 'A X': 'Z', 'B Y': 'Y', 'C Z': 'X', 'A Y': 'X', 'B Z': 'Z', 'C X': 'Y'}

for str2 in adjData:                                             # this for loop works but is rather convoluted, look to minimise in future.
    for key3, value3 in DictStrtgy.items():                        
        if key3 == str2[2]:                                         
            playerscr2.append(value3)                            
            for key4, value4 in DictRevOC.items():
                if str2 == key4:
                    for key5, value5 in DictPlrHnd.items():
                        if key5 == value4:
                            playerscr2.append(value5)
                        else:
                            pass
                else:
                    pass
        else:                                               
            pass

print(sum(playerscr2))  
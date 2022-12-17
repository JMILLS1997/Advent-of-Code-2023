##Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?##

FilePath = "D:\Python\Advent of Code 2022\Challenge 1\Caloric Content List.txt"

OpenFile = open(FilePath,"r")
data = OpenFile.read() ##access data
stringlist = data.split("\n") ##splits each line into list instances

V = 0
newInt = []
intList = []
totalKcals = []

for string in stringlist:               #for any indexed item in the list of strings "stringlist"
    is_int = string.isdigit()           #is_int produces a boolean value depending on data input
    if string == '':                    #if string is a blank space, this is appended to the new list "intList"
        intList.append(string)          
    if is_int == True:                  #if is_int is true, convert the info held in the variable "string" into an interger
        newInt = int(string)            
        intList.append(newInt)          #append new data type into the list "intList"

print(intList)                          #sanity check




























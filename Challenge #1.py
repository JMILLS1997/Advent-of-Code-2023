Challenge #1

##Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?##

FilePath = "D:\Python\Advent of Code 2022\Challenge 1\Caloric Content List.txt"

OpenFile = open(FilePath,"r")
data = OpenFile.read() ##access data

stringlist = data.split("\n") ##splits each line into list instances

intList = []

for string in stringlist:
    is_int = string.isdigit()
    if is_int:
        newInt = int(string)
        intList.append(newInt)
    else is_int:
        newSpace = str("\n")
        intList.append(newSpace)

print(intList) ##All data is missing the blank, seperator between what each elf is carrying.
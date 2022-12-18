##Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?##

FilePath = "D:\Python\Advent of Code 2022\Challenge 1\Caloric Content List.txt"

OpenFile = open(FilePath,"r")
data = OpenFile.read()                  #access data
stringlist = data.split("\n")           #splits each line into list instances

IndvKcal = 0
newInt = []
intList = []
totalKcals = []

for string in stringlist:               #for any indexed item in the list of strings "stringlist"
    is_int = string.isdigit()           #is_int produces a boolean value depending on data input
    if string == '':                    #if string is a blank space, this is appended to the new list "intList"
        intList.append(0)          
    if is_int == True:                  #if is_int is true...
        newInt = int(string)            #convert the info held in the variable "string" into an interger
        intList.append(newInt)          #append new data type into the list "intList"

for num in intList:                     #for any indexed item in list of integers "intList"
    if num != 0:                        #if the indexed value in "intList" does NOT equal 0
        IndvKcal = IndvKcal + num       #add the value to variable "IndvKcal", which has an initial value of 0
    if num == 0:                        #if indexed value is equal to 0
        totalKcals.append(IndvKcal)     #append the value of the "IndvKcal" which signifies the total kcals for an individual elf
        IndvKcal = 0                    #reset IndvKcal to 0 

totalKcals.sort()         #sorts list of total kcals per elf into ascending order                               
print(totalKcals[-1])

#####Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?######

totalKcals.sort(reverse = True)         #sorts list of total kcals per elf into ascending order                               
print(totalKcals[0:3])                  #prints last most value, which is largest due to previous sort function being applied to list "totalKcals"

v = sum(totalKcals[0:3])                     #sum of list values 
print(v)                                #prints sum total of all kcals per elf in list




























finalList = []
yourList = []
ifContinue = 'yes'

while ifContinue == 'yes':
  yourList.append(input("What word do you want to add to your list?: "))
  ifContinue = input("Do you want to add anymore words to the list?(yes/no): ")


def mySlice(yourList, index1, index2):
    for item in range (index1, index2):
        finalList.append(yourList[item])
    return finalList

startingIndex = int(input("What will be the starting index?(integer): "))
endingIndex = int(input("What will be the ending index?(integer): "))
print(mySlice(yourList, startingIndex, endingIndex))

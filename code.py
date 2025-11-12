def mySlice(yourList, index1, index2):
  numberOfItems = index2-index1
  finalList = list.pop(index1, numberOfItems)
  return finalList
mySlice()

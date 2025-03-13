thisdict = {
    "texts": []
}
print("Neçəyə qədər istəyirsən?")
myRange = int(input())
myListHead = 65
myListElement = 120
firstList = []
for j in range(myRange):
  firstList.append(str(j))
  if firstList[0]=="0":
    firstList[0]=chr(42)
thisdict["texts"].append(firstList)
for i in range(myRange):
    newList = []
    newList.append(chr(myListHead))
    myListHead += 1
    for j in range(myRange-1):
        newList.append(chr(myListElement))
    thisdict["texts"].append(newList)
result = '\n'.join(str(x) for x in thisdict['texts'])
print(result)

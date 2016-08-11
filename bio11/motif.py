with open('rosalind_lcsm.txt') as r:
    lineCount= r.readlines()

stringList = []
result = []
name = []
for i in range(0,len(lineCount),18):
    string=''
    name.append(lineCount[i][1:-2])
    for j in range(1,18):
        string+=lineCount[i+j].rstrip()
    stringList.append(string)
length=len(stringList[0])
test=False

while(length>0 and not test):
    for i in range(len(stringList[0])-(length-1)):
        success=True
        substring=stringList[0][i:i+length]
        for j in stringList[1:len(stringList)]:
            if (substring not in j):
                success=False
                break
        if success:
            print(substring)
            test=True
            break
    length-=1

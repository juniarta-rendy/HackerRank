m = int(input())
a = list(map(int, input().split()))

n = int(input())
b = list(map(int, input().split()))

newList = a+b
dell = 0

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            dell = a[i]
            newList.remove(dell)
            break
for i in range(len(b)):
    for j in range(len(a)):
        if b[i] == a[j]:
            dell = b[i]
            newList.remove(dell)
            break

finalList = []
for i in newList:
    if i not in finalList:
        finalList.append(i)
        
for i in range(len(finalList)-1):
    for j in range(len(finalList)-i-1):
        if finalList[j] > finalList[j+1]:
            finalList[j], finalList[j+1] = finalList[j+1], finalList[j]

for i in range(len(finalList)):
    print(finalList[i])
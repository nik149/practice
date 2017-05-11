import sys

N = map(int, raw_input())[0]

arr = map(int, raw_input().split(" "))

allLists = []

for i in range(0, N):
    subList = [arr[i]]
    for j in range(i+1, N):
        if arr[j] >= arr[i]:
            subList.append(arr[j])
    allLists.append(subList)

print allLists

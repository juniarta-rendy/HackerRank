import numpy as np

arr1 = []
arr2 = []
N,M,P = map(int,input().split())

for i in range(N):
    arr1.append(input().split())
for j in range(M):
    arr2.append(input().split())

arr1 = np.array(arr1)
arr2 = np.array(arr2)
newarr = np.concatenate((arr1,arr2))

print(np.array2string(newarr, separator=' ', formatter={'str_kind': lambda x: x}))
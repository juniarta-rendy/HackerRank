import numpy

n,m = map(int,input().split())
arr = []

for _ in range(m):
    arr.append([int (y) for y in input().split()])
    
arr = numpy.sum(arr,axis = 0)
print(numpy.prod(arr))
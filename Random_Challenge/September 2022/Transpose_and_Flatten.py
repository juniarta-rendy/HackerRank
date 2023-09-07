import numpy

myarr = []
matrix = input().split()

for i in range(int(matrix[0])):
    myarr.append([int(j) for j in input().split()])

myarr = numpy.array(myarr)

print(numpy.transpose(myarr))
print(myarr.flatten())
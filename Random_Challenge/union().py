n = int(input())
eng = set(list(map(int, input().split())))
N = int(input())
fre = list(map(int, input().split()))

both = eng.union(fre)

print(len(both))
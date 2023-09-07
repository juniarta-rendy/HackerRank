n = int(input())
s = set(list(map(int, input().split())))
N = int(input())

for i in range(N):
    com = list(input().split())
    if len(com) > 1:
        def case(a,b):
            if a == 'remove':
                s.remove(b)
            elif a == 'discard':
                s.discard(b)
        com[1] = int(com[1])
        case(com[0], com[1])
        
    else:
        s.pop()
print(sum(s))
                
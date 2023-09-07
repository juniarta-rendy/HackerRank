if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    x = max(arr)
    y = -9999
    
    for i in range(n):
        if arr[i] < x and arr[i] > y:
            y = arr[i]
    print(y)
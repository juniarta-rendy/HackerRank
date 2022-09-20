def maxCost(cost, labels, dailyCount):
    c_cost = 0
    c_label = 0
    maxCost = 0
    
    for c,l in zip(cost,labels):
        c_cost += c
        if l == 'illegal':
            continue
        c_label +=1
        if c_label == dailyCount:
            maxCost = max(maxCost,c_cost)
            c_cost = 0
            c_label = 0
    return maxCost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    cost_count = int(input().strip())

    cost = []

    for _ in range(cost_count):
        cost_item = int(input().strip())
        cost.append(cost_item)

    labels_count = int(input().strip())

    labels = []

    for _ in range(labels_count):
        labels_item = input()
        labels.append(labels_item)

    dailyCount = int(input().strip())

    result = maxCost(cost, labels, dailyCount)

    fptr.write(str(result) + '\n')

    fptr.close()
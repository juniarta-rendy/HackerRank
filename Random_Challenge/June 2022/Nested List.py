if __name__ == '__main__':
    names = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
    
    x = min(scores)
    y = 9999
    for i in range(len(scores)):
        if scores[i] > x and scores[i] < y:
            y = scores[i]
    result = []
    
    for j in range(len(scores)):
        if y == scores[j]:
            result.append(names[j])
            
    result = sorted(result)
    for i in range(len(result)):
        print(result[i])
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    person = student_marks[query_name]
    
    def average(avg):
        total = sum(avg)/len(avg)
        total = "{:.2f}".format(total)
        return total
    
    print(average(person))

def mutate_string(string, position, character):
    string = list(string)
    string[position] = character
    newString = ''.join(string)
    return newString

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
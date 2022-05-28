def swap_case(s):
    for i in range(len(s)):
        s = list(s)
        if s[i].isupper():
            s[i]=s[i].lower()
        elif s[i].islower():
            s[i]=s[i].upper()
    s = ''.join(s)
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
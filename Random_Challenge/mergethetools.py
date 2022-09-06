import textwrap

def merge_the_tools(string, k):
    newString = textwrap.wrap(string,k)
    result = []
    for i in range(len(newString)):
        text = ''
        for j in newString[i]:
            if j not in text:
                text += j
        result.append(text)
    for i in range(len(result)):
        print(result[i])

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
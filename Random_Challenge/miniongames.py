def minion_game(string):
    scores = {'Kevin':0,'Stuart':0}
    result = None
    
    for i in range(len(string)):
        if string[i] in 'AIUEO':
            scores['Kevin'] += len(string)-i
        else:
            scores['Stuart'] += len(string)-i
    if scores['Kevin'] == scores['Stuart']:
        result = 'Draw'
    elif scores['Kevin'] > scores['Stuart']:
        result = 'Kevin ' + str(scores['Kevin'])
    else:
        result = 'Stuart ' + str(scores['Stuart'])
    
    return print(result)
    
if __name__ == '__main__':
    s = input()
    minion_game(s)
from collections import defaultdict

def solution(input_string):
    alphabet = defaultdict(int)
    for i, string in enumerate(input_string):
        if i!= 0 and string == input_string[i-1]:
            continue
        if alphabet[string]:
           alphabet[string] += 1
        else:
            alphabet[string] = 1
    
    answer = []
    for i in alphabet:
        if alphabet[i] != 1:
            answer.append(i)
    answer = ''.join(sorted(answer))
    if answer == '':
        answer = 'N'
    return answer

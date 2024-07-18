def distance(pos1, pos2):
    return abs(pos2[0]-pos1[0]) + abs(pos2[1]-pos1[1])

def solution(numbers, hand):
    answer = ''
    numpad = {'1': (0, 0), '4': (0, 1), '7': (0, 2), '2': (1, 0), '5': (1, 1), '8': (1, 2), '0': (1, 3), '3': (2, 0), '6': (2, 1), '9': (2, 2)}
    pos = {'L': [0, 3], 'R': [2, 3]}
    for number in numbers:
        if numpad[str(number)][0] == 0:
            answer += 'L'
            pos['L'] = [0, numpad[str(number)][1]]
        elif numpad[str(number)][0] == 2:
            answer += 'R'
            pos['R'] = [2, numpad[str(number)][1]]
        else:
            L_distance = distance(pos['L'], numpad[str(number)])
            R_distance = distance(pos['R'], numpad[str(number)])
            if L_distance < R_distance:
                answer += 'L'
                pos['L'] = list(numpad[str(number)])
            elif L_distance > R_distance:
                answer += 'R'
                pos['R'] = list(numpad[str(number)])
            if L_distance == R_distance:
                answer += hand[:1].upper()
                pos[hand[:1].upper()] = list(numpad[str(number)])

    return answer

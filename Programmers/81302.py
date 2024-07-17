def solution(places):
    answer = []
    
    for place in places:
        flag = False
        for i in range(5):
            if flag:
                break
            for j in range(5):
                if place[i][j] == 'P':
                    if j != 4 and place[i][j+1] == 'P':
                        flag = True
                        break
                    elif i != 4 and place[i+1][j] == 'P':
                        flag = True
                        break
                    elif i != 4 and j != 4 and place[i+1][j+1] == 'P' and (place[i][j+1] != 'X' or place[i+1][j] != 'X'):
                        flag = True
                        break
                    elif i != 4 and j != 0 and place[i+1][j-1] == 'P' and (place[i][j-1] != 'X' or place[i+1][j] != 'X'):
                        flag = True
                        break
                    elif j < 3 and place[i][j+1] != 'X' and place[i][j+2] == 'P':
                        flag = True
                        break
                    elif i < 3 and place[i+1][j] != 'X' and place[i+2][j] == 'P':
                        flag = True
                        break
        if flag:
            answer.append(0)
        else:
            answer.append(1)
        
    return answer

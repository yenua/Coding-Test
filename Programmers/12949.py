def solution(arr1, arr2):
    answer = []
    #answer = [[0]*len(arr2[0]) for i in range(len(arr1))]
    for i in range(len(arr1)):
        answer.append([])
        for j in range(len(arr2[0])):
            temp = 0
            for k in range(len(arr1[0])):
                temp += arr1[i][k] * arr2[k][j]
            #answer[i][j] = temp
            answer[i].append(temp)
    return answer

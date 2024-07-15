def solution(N, stages):
    states = [[i+1, 0, 0] for i in range(N)]

    for i in stages:
        for j in range(0, i-1):
            states[j][1] += 1
        if i == N+1:
            continue
        states[i-1][2] += 1
    #print(states)

    for i in range(len(states)):
        if states[i][1]+states[i][2] == 0:
            continue
        states[i][1] = states[i][2]/(states[i][1]+states[i][2])
    #print(states)
    states.sort(key=lambda x: (x[1], -x[0]), reverse=True)
    #print(states)

    answer = []
    for i in states:
        answer.append(i[0])
    return answer

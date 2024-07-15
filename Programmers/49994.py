def solution(dirs):
    memo = []
    pre = (5, 5)
    direction = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    
    answer = 0
    
    for i in dirs:
        if i == 'U':
            now = (pre[0]+direction[0][0], pre[1]+direction[0][1])
        elif i == 'D':
            now = (pre[0]+direction[1][0], pre[1]+direction[1][1])
        elif i == 'R':
            now = (pre[0]+direction[2][0], pre[1]+direction[2][1])
        elif i == 'L':
            now = (pre[0]+direction[3][0], pre[1]+direction[3][1])
        if 0 <= now[0] <= 10 and 0 <= now[1] <= 10:
            if (pre, now) not in memo and (now, pre) not in memo:
                memo.append((pre, now))
                answer += 1
            #print(memo)
            pre = now
            
            
    return answer

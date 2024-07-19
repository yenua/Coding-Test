from bisect import bisect_left, bisect_right

def solution(tickets):
    answer = []
    used = [False] * len(tickets)
    tickets.sort(key=lambda x: (x[0], x[1]))
    first = [x[0] for x in tickets]
    def dfs(now):
        if False not in used:
            return True
        if bisect_left(first, now) == bisect_right(first, now):
            return False
        for i in range(bisect_left(first, now), bisect_right(first, now)):
            if not used[i]:
                used[i] = True
                if dfs(tickets[i][1]):
                    answer.append(tickets[i][1])
                    return True
                used[i] = False
        return False
            
    for i, ticket in enumerate(tickets):
        if ticket[0] == 'ICN':
            used[i] = True
            if dfs(ticket[1]):
                answer.append(ticket[1])
                answer.append(ticket[0])
                break
            used[i] = False
    return answer[::-1]

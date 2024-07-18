def solution(participant, completion):
    participant.sort()
    completion.sort()
    length = len(participant)
    for i in range(length-1):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[length - 1]

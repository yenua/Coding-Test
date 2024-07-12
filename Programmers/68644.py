def solution(numbers):
    temp = []
    length = len(numbers)
    for i in range(length-1):
        for j in range(i+1, length):
            temp.append(numbers[i]+numbers[j])
    answer = list(set(temp))
    answer.sort()
    return answer

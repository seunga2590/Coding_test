def solution(array, n):
    answer = [0] * len(range(0, max(array)+1))
    for i in range(len(array)):
        if array[i] in array:
            answer[array[i]] += 1
        else:
            answer += 0

    return answer[n]
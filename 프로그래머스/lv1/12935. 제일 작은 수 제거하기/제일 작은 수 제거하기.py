def solution(arr):
    answer = []
    if len(arr) > 1:
        answer = arr
        answer.remove(min(answer))
    else:
        answer.append(-1)
    return answer
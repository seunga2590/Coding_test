def solution(n):
    answer = 1
    r =6
    while True:
        if (r*answer) % n == 0:
            break
        else:
            answer+= 1
    return answer
def solution(n):
    answer = []
    for i in range(1, n):
        if n % i == 1:
            answer.append(i)
        else:
            pass
    answer = min(answer)
    
    return answer
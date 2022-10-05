def solution(x, n):
    answer = []
    
    for i in range(n):
        value = x + i*x
        answer.append(value)
    
    return answer
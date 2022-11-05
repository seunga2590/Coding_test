def solution(n):
    answer = 0
    num = n**(1/2)
    
    if int(num) * int(num) == n:
        answer = 1
    else:
        answer = 2
    return answer
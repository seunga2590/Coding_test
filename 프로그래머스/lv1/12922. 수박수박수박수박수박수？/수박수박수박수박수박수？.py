def solution(n):
    answer = ''
    word = '수박'
    
    if n % 2 == 0:
        answer = answer + word * int(n/2)
    elif n % 2 == 1:
        answer = answer + word * int(n//2) + word[:1]
    
    return answer
# 1) 수정한 풀이
def solution(x, n):
    answer = []
    
    for i in range(n):
        value = x + i*x
        answer.append(value)
    
    return answer

# 2) 기존 풀이
def solution(x, n):
    answer = []
    
    if x>0:
        for i in range(x, (i*x)+1, x):
            answer.append(i)
    elif x<0:
        for i in range((i*x), x+1, abs(x)):
            answer.append(i)
            answer.sort(reverse=True)
    
    return answer

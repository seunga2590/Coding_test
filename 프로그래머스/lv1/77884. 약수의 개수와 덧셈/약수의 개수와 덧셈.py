def make_divisor(n):
    div = []
    for i in range(1, n+1):
        if n % i == 0:
            div.append(i)
    return div

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if len(make_divisor(i)) % 2 == 0:
            answer += i
        else:
            answer -= i
            
    return answer
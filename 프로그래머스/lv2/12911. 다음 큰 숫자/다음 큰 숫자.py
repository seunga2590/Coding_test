def divisor_2(num):
    answer = 1

    while num > 1:
        if num % 2 == 1:
            answer += 1
        else:
            answer += 0
        
        num = num // 2
    return answer

def solution(n):
    final_answer = 0
    for i in range(n+1, 1000001):
        if divisor_2(n) == divisor_2(i):
            final_answer = i
            break
    return final_answer
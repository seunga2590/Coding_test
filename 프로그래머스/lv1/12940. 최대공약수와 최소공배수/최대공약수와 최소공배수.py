def solution(n, m):
    answer = []
    final_ans = []
    #최대공약수
    if m < n :
        n, m = m, n
    for i in range(1, m+1):
        if n % i ==0 and m % i == 0:
            answer.append(i)
    
    answer = answer[-1]

    chidae = answer
    chiso = chidae * (n/chidae) * (m/chidae) #최소공배수 
    
    answer = [chidae,chiso]
    return answer

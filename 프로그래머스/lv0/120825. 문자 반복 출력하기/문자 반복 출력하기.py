def solution(my_string, n):
    answer = ''
    
    for i in my_string:
        if type(i) == str:
            answer += i*n
        else:
            pass
    
    return answer
        
        
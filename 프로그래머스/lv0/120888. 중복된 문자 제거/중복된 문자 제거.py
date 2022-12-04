def solution(my_string):
    result = []
    for value in my_string:
        if value not in result:
            result.append(value)
            
    answer = ''.join(result)
    return answer
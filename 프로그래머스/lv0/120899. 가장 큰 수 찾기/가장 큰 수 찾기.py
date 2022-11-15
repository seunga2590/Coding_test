def solution(array):
    answer = []
    
    max_num = max(array)
    answer.append(max_num)
    idx = array.index(max_num)
    answer.append(idx)
    
    return answer
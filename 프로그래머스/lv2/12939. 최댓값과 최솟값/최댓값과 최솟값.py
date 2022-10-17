def solution(s):
    data = ''
    answer = []
    s = s.split(' ')
    for i in s:
        answer.append(int(i))
        answer = sorted(answer)
    
    data += str(answer[0])
    data += ' '
    data += str(answer[-1])
    
    return data
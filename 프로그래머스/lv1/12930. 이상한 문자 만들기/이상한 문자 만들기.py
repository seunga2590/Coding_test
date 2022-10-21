def solution(s):
    answer = s.split(' ')
    fin = ''
    for i in answer:
        for num, j in enumerate(i):
            if num % 2 ==0:
                fin += j.upper()
            else:
                fin += j.lower()
        fin += ' '
    return fin[:-1]
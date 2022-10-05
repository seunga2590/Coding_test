def solution(s):
    a = 0
    b = 0
    for i in s:
        i = i.lower()
        if i == 'p':
            a += 1
        else:
            b += 1
    if a == b:
        print('true')
    else:
        print('false')  
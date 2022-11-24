def solution(order):
    order = list(str(order))
    s = 0
    for i in order:
        if int(i)%3 ==0 and int(i) != 0:
            s += 1
    return s
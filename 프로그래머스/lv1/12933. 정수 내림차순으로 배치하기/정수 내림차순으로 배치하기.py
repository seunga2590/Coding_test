def solution(n):
    value = []
    for i in str(n):
        value.append(i)
        value.sort(reverse = True)
    return int(''.join(value))
        
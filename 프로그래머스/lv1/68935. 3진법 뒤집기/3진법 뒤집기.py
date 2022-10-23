def solution(n):
    a = []
    b = []

    while n >=1:
        a.append(n % 3)
        n = n //3
    for i in range(len(a)):
        b.append((3**i) * a[::-1][i])
    return sum(b)
def solution(price, money, count):
    a =0
    for i in range(count):
        a += (price + price*i)
        answer = money - a
        

    if answer > 0:
        return 0
    else:
        return abs(answer)
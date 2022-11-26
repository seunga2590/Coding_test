def solution(age):
    answer = ''
    aa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    for i in str(age):
        answer += aa[int(i)]
    return answer
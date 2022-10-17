def solution(s):
    answer = []
    for i in range(len(s)):
        if s[i-1] == " ":
            answer.append(s[i].upper())
        elif i == 0:
            answer.append(s[0].upper())
        else:
            answer.append(s[i].lower())
    return ''.join(answer)
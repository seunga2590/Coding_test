def solution(participant, completion):
    data = ''
    answer = {}
    for p in participant:
        if p in answer:
            answer[p] += 1
        else:
            answer[p] = 1
        
    for p in completion:
        if answer[p] == 1:
            del answer[p]
        else:
            answer[p] -= 1

    data = list(answer.keys())[0]
    return data
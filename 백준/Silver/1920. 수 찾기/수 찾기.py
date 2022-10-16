a = int(input())
b = set(map(int, input().split())) #list에서 변경
c = int(input())
d = list(map(int, input().split()))

#b = sorted(b)

for i in d:
    if i in b:
        print(1)
    else:
        print(0)
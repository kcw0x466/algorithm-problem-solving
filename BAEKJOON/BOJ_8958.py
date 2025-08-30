T=int(input())
i=0
cnt=0
total=0
scores=[]
while i<T:
    ox=input()
    for c in ox:
        if c=='O':
            cnt+=1
            total+=cnt
        elif c=='X':
            cnt=0
            total+=cnt
    scores.append(total)
    total=0
    cnt=0
    i+=1

for s in scores:
    print(s)
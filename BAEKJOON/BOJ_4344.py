T=int(input())
percent=[]

cnt=0
while cnt<T:
    scores=tuple(map(int, input().split()))
    sum=0
    for i in range(1,scores[0]+1):
        sum+=scores[i]
    avg=sum/scores[0]
    avg_over=0
    for i in range(1,scores[0]+1):
        if scores[i]>avg:
            avg_over+=1
    percent.append(round((avg_over/scores[0])*100,3))
    cnt+=1

for p in percent:
    print("{:.3f}%".format(p))
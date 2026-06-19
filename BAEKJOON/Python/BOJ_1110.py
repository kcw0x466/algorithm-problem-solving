init=int(input())
N=init
cnt=0
while True:
    N=((N%10)*10)+(((N//10)+(N%10))%10)
    cnt+=1
    if N==init:
        break

print(cnt)

N=int(input())

def HanSuCnt(n):
    
    if n<100:
        return n
    else:
        cnt=99
        for i in range(100,N+1):
            hun=i//100
            ten=(i//10)%10
            one=i%10
            if (hun-ten)==(ten-one):
                cnt+=1

    return cnt

print(HanSuCnt(N))

    
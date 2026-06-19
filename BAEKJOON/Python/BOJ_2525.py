A,B=map(int, input().split())
C=int(input())

if(B+C<60):
    H=A
    M=B+C
else:
    H=A+((B+C)//60)
    M=(B+C)%60
    if(H>23):
        H=H-24

print(H, M)
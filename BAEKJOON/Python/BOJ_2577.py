A=int(input())
B=int(input())
C=int(input())
result=str(A*B*C)

nums=list(set(result))
num_count={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}

for c in nums:
    num_count[c]=result.count(c)

for i in range(10):
    print(num_count[str(i)])


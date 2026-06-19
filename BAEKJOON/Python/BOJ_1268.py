# BOJ 1268

N = int(input())
data = []
cntList = []
for _ in range(N):
    data.append(list(map(int, input().split())))
for s in range(N):
    cnt = 0
    for c in range(5):
        for r in range(N):
            if  s != c and data[s][c] == data[r][c]:
                cnt += 1
    cntList.append(cnt)
print(cntList.index(max(cntList)) + 1)

# https://zzang9ha.tistory.com/110 참고
# 예를들어 1번 학생이랑 2번 학생이 같은반 된적이 2번 이상이면 같은반이었던 학생수 1명으로 간주함 -> 중복 문제 해결해야함
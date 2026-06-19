N, M = map(int, input().split())
nums = [int(input()) for _ in range(N)]
result = []
for _ in range(M):
    a, b = map(int, input().split())
    result.append(min(nums[a - 1:b]))
for ans in result:
    print(ans)
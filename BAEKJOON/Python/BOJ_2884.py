H,M=map(int, input().split())
time=0
if (H==0) and (M<45):
    time=24*60+M
else:
    time=H*60+M
time-=45
print(f'{time//60} {time%60}')
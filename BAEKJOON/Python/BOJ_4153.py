while True:
    lengths=list(map(int, input().split()))
    max_=max(lengths)
    if sum(lengths)==0:
        break
    lengths.remove(max_)
    if pow(max_,2)==pow(lengths[0],2)+pow(lengths[1],2):
        print('right')
    else:
        print('wrong')
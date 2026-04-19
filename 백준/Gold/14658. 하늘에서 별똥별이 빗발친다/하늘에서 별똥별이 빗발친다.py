N, M, L, K=map(int,input().split())
star=[list(map(int,input().split())) for i in range(K)]
r=0
for i in star:
    for j in star:
        x = 0
        for k in star:
            if i[0] <= k[0] <= i[0]+L and j[1] <= k[1] <= j[1]+L:
                x+=1
            r = max(r,x)
print(K-r)
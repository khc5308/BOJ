d,h,m=map(int,input().split())
r=(d*24+h)*60+m
print(-1 if r<16511 else r-16511)
a,b,c=map(int,input().split(":"))
x,y,z=map(int,input().split(":"))
r1 = a*3600+b*60+c 
r2 = x*3600+y*60+z
if r1 < r2:
    print(max(r2,r1)-min(r2,r1))
else:
    print(86400-r1+r2)
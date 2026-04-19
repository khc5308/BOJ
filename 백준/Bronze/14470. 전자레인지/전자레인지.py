a,b,c,d,e=[int(input()) for _ in range(5)]
r = -a*c+b*e+d if a<0 else (b-a)*e
print(r)
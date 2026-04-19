n,u,l=map(int,input().split())
a=n>=1000
print("Very Good"if a and(u>=8000 or l>=260)else"Good"if a else"Bad")
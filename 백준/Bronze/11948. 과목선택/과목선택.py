a=[int(input()) for i in range(6)]
print(sum(sorted(a[:4],reverse=1)[:3])+sorted(a[4:],reverse=1)[0])
n = []
for _ in range(28):
    n.append(int(input()))
for i in range(1,31):
    if n.count(i) == 0:
        print(i) 
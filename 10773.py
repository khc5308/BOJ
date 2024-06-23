n = int(input())
m = []
sum = 0
for i in range(n):
    input_ = int(input())
    if input_ == 0:
        m.pop()
    else:
        m.append(input_)

for i in range(len(m)):
    sum += m[i]

print(sum)
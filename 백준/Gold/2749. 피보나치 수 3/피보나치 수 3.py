n = int(input())
dp = [0,1]

m = 1000000
p = 15 * 100000 

for i in range(2,p):
    dp.append((dp[i-1] + dp[i-2]) % m)

print(dp[n%p])
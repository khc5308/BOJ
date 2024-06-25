a , b = map(int,input().split())

def gcd(a, b) :
  while (b != 0) :
    r = a % b
    a = b
    b = r
  
  return a

print(gcd(a,b))
print(int((a * b) / gcd(a, b)))
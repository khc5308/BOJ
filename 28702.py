a = input()
b = input()
c = input()
if not a.isalpha():
    a = int(a)
    next = a + 3
elif not b.isalpha():
    b = int(b)
    next = b + 2
elif not c.isalpha():
    c = int(c)
    next = c + 1

if next%15 == 0:
    print("FizzBuzz")
elif next%3 == 0:
    print("Fizz")
elif next%5 == 0:
    print("Buzz")
else:
    print(next)

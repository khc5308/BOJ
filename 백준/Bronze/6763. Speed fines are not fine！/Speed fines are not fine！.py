a=-int(input())+int(input())
print("Congratulations, you are within the speed limit!"if a<=0 else"You are speeding and your fine is ${}.".format(100 if a<21 else 270 if a<31 else 500))
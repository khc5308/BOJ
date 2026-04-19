kg=float(input())
m=float(input())
bmi=kg/m**2
print(["Under","Normal ","Over"][int(bmi>25)*2+int(18.5<=bmi<=25)]+"weight")
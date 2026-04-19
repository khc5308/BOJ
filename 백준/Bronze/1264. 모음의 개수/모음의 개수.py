while(1):
    a = input()
    mo = 0
    if (a == '#'):
        break
    for i in range(len(a)):
        if (a[i] == 'a' or a[i] == 'e' or a[i] == 'o' or a[i] == 'u' or a[i] == 'i' or a[i] == 'A' or a[i] == 'E' or a[i] == 'O' or a[i] == 'U' or a[i] == 'I'):
            mo += 1
    print(mo)
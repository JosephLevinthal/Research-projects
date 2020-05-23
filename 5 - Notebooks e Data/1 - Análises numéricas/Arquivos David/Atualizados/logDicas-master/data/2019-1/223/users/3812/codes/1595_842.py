num = int(input('digite num: '))
n1 = num // 1000
n2 = (num - 1000*n1) // 100
n3 = (num - 1000*n1 - 100*n2) // 10
n4 = num - 1000*n1 - 100*n2 - n3*10

verif = (n1+n2+n3+n4)

print(verif)